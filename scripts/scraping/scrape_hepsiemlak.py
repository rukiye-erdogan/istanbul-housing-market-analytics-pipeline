import sys
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# ------------------------------------------------------------
# Configuration
# ------------------------------------------------------------

URL = "https://www.hepsiemlak.com/istanbul-satilik/residence-site-ici"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_OUTPUT = PROJECT_ROOT / "data/raw/istanbul_residence_pipeline.csv"
SNAPSHOT_DIR = PROJECT_ROOT / "data/snapshots"
DEBUG_DIR = PROJECT_ROOT / "logs/debug"

WAIT_SECONDS = 45
CHROME_MAJOR_VERSION = 150

LISTING_SELECTOR = 'li[class*="listing"]'

BLOCKING_TERMS = (
    "captcha",
    "güvenlik doğrulaması",
    "security verification",
    "verify you are human",
    "robot olmadığınızı",
    "access denied",
    "erişim engellendi",
    "cloudflare",
    "unusual traffic",
)


def create_driver():
    """Create and return the configured Chrome driver."""
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-allow-origins=*")

    return uc.Chrome(
        options=options,
        version_main=CHROME_MAJOR_VERSION,
    )


def accept_cookies(driver):
    """Close the cookie dialog when it is present."""
    possible_buttons = (
        (By.XPATH, "//button[contains(normalize-space(), 'Kabul Et')]"),
        (By.XPATH, "//button[contains(normalize-space(), 'Accept')]"),
        (By.XPATH, "//button[contains(normalize-space(), 'Alle akzeptieren')]"),
    )

    for locator in possible_buttons:
        try:
            button = WebDriverWait(driver, 4).until(
                EC.element_to_be_clickable(locator)
            )
            driver.execute_script(
                "arguments[0].click();",
                button,
            )
            print("Cookie banner accepted.")
            return
        except TimeoutException:
            continue
        except Exception as exc:
            print(f"Cookie banner could not be closed: {exc}")
            return

    print("No cookie banner requiring confirmation was found.")


def page_is_blocked(driver):
    """Return True when the visible page resembles a blocking page."""
    page_text = driver.page_source.lower()
    title = (driver.title or "").lower()

    return any(
        term in page_text or term in title
        for term in BLOCKING_TERMS
    )


def save_debug_information(driver):
    """Store diagnostic files for failed automated runs."""
    DEBUG_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot = DEBUG_DIR / f"scraper_failure_{timestamp}.png"
    html_file = DEBUG_DIR / f"scraper_failure_{timestamp}.html"

    try:
        driver.save_screenshot(str(screenshot))
        print(f"Debug screenshot: {screenshot}")
    except Exception as exc:
        print(f"Screenshot could not be saved: {exc}")

    try:
        html_file.write_text(
            driver.page_source,
            encoding="utf-8",
        )
        print(f"Debug HTML: {html_file}")
    except Exception as exc:
        print(f"Debug HTML could not be saved: {exc}")


def wait_for_listings(driver):
    """Wait until at least one real-estate listing is available."""
    print(
        f"Waiting up to {WAIT_SECONDS} seconds "
        "for the listing results..."
    )

    try:
        WebDriverWait(driver, WAIT_SECONDS).until(
            lambda current_driver: len(
                current_driver.find_elements(
                    By.CSS_SELECTOR,
                    LISTING_SELECTOR,
                )
            ) > 0
        )
    except TimeoutException as exc:
        if page_is_blocked(driver):
            raise RuntimeError(
                "Security verification or access blocking detected. "
                "The automated run was stopped safely."
            ) from exc

        raise RuntimeError(
            "The listing results did not appear within "
            f"{WAIT_SECONDS} seconds."
        ) from exc


def extract_listing(listing):
    """Extract one listing into a normalized dictionary."""
    listing_text = listing.text
    lines = listing_text.splitlines()

    try:
        link_element = listing.find_element(By.TAG_NAME, "a")
        listing_url = link_element.get_attribute("href") or "no_url"
    except Exception:
        listing_url = "no_url"

    if listing_url != "no_url":
        listing_id = listing_url.rstrip("/").split("-")[-1]
    else:
        listing_id = (
            f"temp_{datetime.now().timestamp()}"
        )

    price = 0

    for line in lines:
        if "TL" not in line:
            continue

        cleaned_price = (
            line.replace("TL", "")
            .replace(".", "")
            .replace(",", "")
            .strip()
        )

        try:
            price = int(cleaned_price)
        except ValueError:
            price = 0

        break

    location = ""

    for line in lines:
        if "İstanbul /" in line:
            location = line
            break

    district = ""
    neighborhood = ""

    try:
        parts = [
            part.strip()
            for part in location.split("/")
        ]

        if len(parts) >= 2:
            district = parts[1]

        if len(parts) >= 3:
            neighborhood = parts[2]
    except Exception:
        pass

    return {
        "listing_id": listing_id,
        "listing_url": listing_url,
        "price": price,
        "district": district,
        "neighborhood": neighborhood,
        "is_in_complex": True,
        "scraped_at": datetime.now(),
    }


def export_data(all_data):
    """Validate and export the current and daily snapshots."""
    if not all_data:
        raise RuntimeError(
            "No valid listings were extracted. "
            "Existing CSV files were not overwritten."
        )

    dataframe = pd.DataFrame(all_data)
    dataframe = dataframe.drop_duplicates(
        subset=["listing_id"]
    )

    if dataframe.empty:
        raise RuntimeError(
            "The extracted data is empty after duplicate removal."
        )

    RAW_OUTPUT.parent.mkdir(
        parents=True,
        exist_ok=True,
    )
    SNAPSHOT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    today = datetime.now().strftime("%Y-%m-%d")
    snapshot_file = (
        SNAPSHOT_DIR / f"snapshot_{today}.csv"
    )

    dataframe.to_csv(
        RAW_OUTPUT,
        index=False,
    )
    dataframe.to_csv(
        snapshot_file,
        index=False,
    )

    print()
    print(dataframe.head())
    print()
    print(
        f"Total Unique Listings: {len(dataframe)}"
    )
    print(
        f"Current CSV exported: {RAW_OUTPUT}"
    )
    print(
        f"Daily snapshot exported: {snapshot_file}"
    )


def main():
    driver = None

    try:
        print("=" * 60)
        print("Hepsiemlak Automated Scraper")
        print(datetime.now())
        print("=" * 60)

        driver = create_driver()

        print(f"Opening: {URL}")
        driver.get(URL)

        accept_cookies(driver)
        wait_for_listings(driver)

        print("Page loaded successfully.")
        print(f"Page Title: {driver.title}")

        titles = driver.find_elements(
            By.TAG_NAME,
            "h1",
        )

        for title in titles:
            if title.text.strip():
                print(title.text.strip())

        listings = driver.find_elements(
            By.CSS_SELECTOR,
            LISTING_SELECTOR,
        )

        print(
            f"Number of listings found: {len(listings)}"
        )

        all_data = []

        for listing in listings:
            try:
                all_data.append(
                    extract_listing(listing)
                )
            except Exception as exc:
                print(
                    f"Listing could not be processed: {exc}"
                )

        export_data(all_data)

        print()
        print("Scraper finished successfully.")
        return 0

    except Exception as exc:
        print()
        print(f"SCRAPER ERROR: {exc}")

        if driver is not None:
            save_debug_information(driver)

        return 1

    finally:
        if driver is not None:
            print("Closing Chrome automatically...")

            try:
                driver.quit()
            except Exception as exc:
                print(
                    f"Chrome could not be closed cleanly: {exc}"
                )


if __name__ == "__main__":
    sys.exit(main())
