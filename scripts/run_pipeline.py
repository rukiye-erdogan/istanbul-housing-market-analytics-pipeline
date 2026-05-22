import os
import requests
import pandas as pd
from pandas.errors import EmptyDataError
from dotenv import load_dotenv
from scripts.processing.exchange_rates import get_exchange_rates

# Load .env
load_dotenv()

# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------
# NO NEW LISTINGS IMAGES
# ---------------------------------------------------------

TOP_IMAGE = os.path.join(
    BASE_DIR,
    "images",
    "woaw_3_EMOJI.png"
)

BOTTOM_IMAGE = os.path.join(
    BASE_DIR,
    "images",
    "peace_4_EMOJI.png"
)

# ---------------------------------------------------------
# NEW LISTINGS IMAGES
# ---------------------------------------------------------

NEW_TOP_IMAGE = os.path.join(
    BASE_DIR,
    "images",
    "schlaubi_2_EMOJI.png"
)

NEW_BOTTOM_IMAGE = os.path.join(
    BASE_DIR,
    "images",
    "daumenhoch_1_EMOJI.png"
)

# ---------------------------------------------------------
# DATA PATHS
# ---------------------------------------------------------

DATA_RAW = os.path.join(
    BASE_DIR,
    "data",
    "raw",
    "istanbul_residence_pipeline.csv"
)

DATA_HIST = os.path.join(
    BASE_DIR,
    "data",
    "historical",
    "istanbul_residence_history.csv"
)

DATA_PROC = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "istanbul_residence_cleaned.csv"
)

print("Running Housing Analytics Pipeline...")

# =========================================================
# TELEGRAM CONFIG
# =========================================================

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

TELEGRAM_URL = (
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
)

TELEGRAM_PHOTO_URL = (
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
)

# =========================================================
# LOAD CURRENT DATA
# =========================================================

try:

    current_df = pd.read_csv(DATA_RAW)

except EmptyDataError:

    print("CSV is empty. No listings scraped.")
    exit()

except FileNotFoundError:

    print("Pipeline CSV file not found.")
    exit()

if current_df.empty:

    print("No listings found. Pipeline stopped.")
    exit()

# =========================================================
# LOAD HISTORY
# =========================================================

try:

    history_df = pd.read_csv(DATA_HIST)

except FileNotFoundError:

    print("History file not found. Creating empty DataFrame.")

    history_df = pd.DataFrame(
        columns=["listing_id"]
    )

# =========================================================
# REMOVE DUPLICATES
# =========================================================

current_df = current_df.drop_duplicates(
    subset=["listing_id"]
)

history_df = history_df.drop_duplicates(
    subset=["listing_id"]
)

# =========================================================
# DETECT NEW LISTINGS
# =========================================================

new_listings = current_df[
    ~current_df["listing_id"].isin(
        history_df["listing_id"]
    )
]

print(
    f"New Listings Found: {len(new_listings)}"
)

# =========================================================
# EXPORT CLEANED DATA
# =========================================================

os.makedirs(
    os.path.dirname(DATA_PROC),
    exist_ok=True
)

current_df.to_csv(
    DATA_PROC,
    index=False
)

print(
    "Cleaned CSV exported successfully."
)

# =========================================================
# FX RATES
# =========================================================

fx = get_exchange_rates()

usd_try = fx["USDTRY"]
eur_try = fx["EURTRY"]

# =========================================================
# NEW LISTINGS FOUND
# =========================================================

if len(new_listings) > 0:

    print("\n🔥 NEW LISTINGS DETECTED:\n")

    for _, row in new_listings.iterrows():

        price = row["price"]

        price_usd = round(price / usd_try)
        price_eur = round(price / eur_try)

        # =================================================
        # MESSAGE
        # =================================================

        message = f"""
🤩🏡 Guten Morgen! ☀️💫

Ein neuer Istanbul-Schatz könnte auf dich warten 💎✨

📍 Bezirk: {row['district']}
🏘 Stadtteil: {row['neighborhood']}

💰 Kaufpreis:
🇹🇷 {price:,.0f} TL
🇺🇸 ${price_usd:,.0f}
🇪🇺 €{price_eur:,.0f}

🕒 Neu im Markt seit:
{row['scraped_at']}

🔗 Direkt zum Angebot:
{row['listing_url']}

🤝 Vielleicht ist das bereits dein nächstes Traumobjekt 🥳🏡✨

Viel Erfolg bei der Jagd nach besonderen Immobilien in Istanbul 🌸💫
"""

        print(message)

        # =================================================
        # 1. SEND TOP IMAGE
        # =================================================

        if os.path.exists(NEW_TOP_IMAGE):

            with open(NEW_TOP_IMAGE, "rb") as photo:

                photo_response = requests.post(
                    TELEGRAM_PHOTO_URL,
                    data={
                        "chat_id": CHAT_ID
                    },
                    files={
                        "photo": photo
                    }
                )

            print(
                "Telegram New Top Photo Status:",
                photo_response.status_code
            )

        else:

            print(
                f"Warnung: Bild nicht gefunden unter {NEW_TOP_IMAGE}"
            )

        # =================================================
        # 2. SEND TEXT MESSAGE
        # =================================================

        payload = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.post(
            TELEGRAM_URL,
            data=payload
        )

        print(
            "Telegram Text Status:",
            response.status_code
        )

        # =================================================
        # 3. SEND BOTTOM IMAGE
        # =================================================

        if os.path.exists(NEW_BOTTOM_IMAGE):

            with open(NEW_BOTTOM_IMAGE, "rb") as photo:

                photo_response = requests.post(
                    TELEGRAM_PHOTO_URL,
                    data={
                        "chat_id": CHAT_ID
                    },
                    files={
                        "photo": photo
                    }
                )

            print(
                "Telegram New Bottom Photo Status:",
                photo_response.status_code
            )

        else:

            print(
                f"Warnung: Bild nicht gefunden unter {NEW_BOTTOM_IMAGE}"
            )

        print(
            "--- Listing erfolgreich verarbeitet ---\n"
        )

# =========================================================
# NO NEW LISTINGS
# =========================================================

else:

    # =====================================================
    # SEND TOP IMAGE
    # =====================================================

    if os.path.exists(TOP_IMAGE):

        with open(TOP_IMAGE, "rb") as photo:

            photo_response = requests.post(
                TELEGRAM_PHOTO_URL,
                data={
                    "chat_id": CHAT_ID
                },
                files={
                    "photo": photo
                }
            )

        print(
            "Telegram Top Photo Status:",
            photo_response.status_code
        )

    else:

        print(
            f"Warnung: Bild nicht gefunden unter {TOP_IMAGE}"
        )

    # =====================================================
    # SEND TEXT
    # =====================================================

    message = """
🤩🏡 Guten Morgen 🌻💫

Der Markt bleibt aktuell ruhig, daher wurden seit dem letzten Update keine neuen passenden Residence-Angebote gefunden.

🤓 Aber keine Sorge — ich beobachte Istanbul weiterhin aufmerksam für dich! 💼

📊 In 2 Tagen erfolgt der nächste automatische Markt-Scan 👍

Bis dahin:

Bleib gesund, munter und dem Markt immer einen Schritt voraus ✌️💫💫💫
"""

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        TELEGRAM_URL,
        data=payload
    )

    print(
        "Telegram Text Status:",
        response.status_code
    )

    # =====================================================
    # SEND BOTTOM IMAGE
    # =====================================================

    if os.path.exists(BOTTOM_IMAGE):

        with open(BOTTOM_IMAGE, "rb") as photo:

            photo_response = requests.post(
                TELEGRAM_PHOTO_URL,
                data={
                    "chat_id": CHAT_ID
                },
                files={
                    "photo": photo
                }
            )

        print(
            "Telegram Bottom Photo Status:",
            photo_response.status_code
        )

    else:

        print(
            f"Warnung: Zweites Bild nicht gefunden unter {BOTTOM_IMAGE}"
        )

# =========================================================
# FINISHED
# =========================================================

print("Pipeline Finished!")