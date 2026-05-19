import time
from datetime import datetime

import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By


# -----------------------------
# Chrome Driver Configuration
# -----------------------------

options = uc.ChromeOptions()

options.add_argument("--start-maximized")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-allow-origins=*")


# -----------------------------
# Start Browser
# -----------------------------

driver = uc.Chrome(options=options)

url = "https://www.hepsiemlak.com/istanbul-satilik/residence-site-ici"
driver.get(url)

time.sleep(15)

input("Complete the security verification and press ENTER...")


# -----------------------------
# Page Information
# -----------------------------

titles = driver.find_elements(By.TAG_NAME, "h1")

for title in titles:
    print(title.text)

print("Page Title:", driver.title)


# -----------------------------
# Extract Listings
# -----------------------------

listings = driver.find_elements(By.CLASS_NAME, "listing-item")

print("Number of listings found:", len(listings))

all_data = []


# -----------------------------
# Process Listings
# -----------------------------

for listing in listings:

    try:

        listing_text = listing.text
        lines = listing_text.split("\n")

        # Extract price
        price = ""

        for line in lines:
            if "TL" in line:
                price = line
                break

        # Clean price
        price = price.replace("TL", "")
        price = price.replace(".", "")
        price = price.replace(",", "")
        price = price.strip()

        price = int(price)

        # Extract location
        location = ""

        for line in lines:
            if "İstanbul /" in line:
                location = line
                break

        parts = location.split("/")

        district = parts[1].strip()
        neighborhood = parts[2].strip()

        # Create listing dictionary
        listing_data = {
            "listing_id": "temp_id",
            "price": price,
            "district": district,
            "neighborhood": neighborhood,
            "is_in_complex": True,
            "scraped_at": datetime.now()
        }

        all_data.append(listing_data)

    except Exception as e:
        print("ERROR:", e)


# -----------------------------
# Create DataFrame
# -----------------------------

df = pd.DataFrame(all_data)

print(df.head())


# -----------------------------
# Export CSV
# -----------------------------

df.to_csv(
    "istanbul_residence_pipeline.csv",
    index=False
)

print("CSV file successfully exported.")


# -----------------------------
# Close Browser
# -----------------------------

input("Press ENTER to close browser...")

driver.quit()