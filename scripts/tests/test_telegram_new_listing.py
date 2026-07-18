from pathlib import Path
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv(Path(".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    raise SystemExit(
        "❌ TELEGRAM_BOT_TOKEN oder TELEGRAM_CHAT_ID fehlt in der .env-Datei."
    )

TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

WOW_BEAR_ID = "5224643461487044408"
BRIEFCASE_BEAR_ID = "5222357516683353476"
GLASSES_BEAR_ID = "5224238334401876298"
THUMBSUP_BEAR_ID = "5222122852555201410"

WOW_BEAR = "🤩"
BRIEFCASE_BEAR = "💼"
GLASSES_BEAR = "🤓"
THUMBSUP_BEAR = "👍"

message = f"""👋 Hi, nice to see you {WOW_BEAR} again!

A new gem in Istanbul might be waiting for {BRIEFCASE_BEAR} you! ✨

📍 District: Kağıthane
🏘 Neighborhood: Emniyet Evleri Mah.

💰 Purchase price:
🇹🇷 12.750.000 TL
🇺🇸 270,701 $
🇪🇺 236.461 €

🕒 Listed on the market since:
17 Jul 2026 · 14:59

🔗 Direct link to the listing:
https://www.hepsiemlak.com/istanbul-kagithane-emniyet-evleri-satilik/residence/81240-12525

🤝 Perhaps this is already your next ✨ dream property! {GLASSES_BEAR}

💫🍀 Good luck in your search for special properties in Istanbul! 🍀💫 {THUMBSUP_BEAR}"""


def utf16_length(text: str) -> int:
    return len(text.encode("utf-16-le")) // 2


def custom_emoji_entity(
    full_text: str,
    emoji: str,
    emoji_id: str,
) -> dict:
    position = full_text.index(emoji)

    return {
        "type": "custom_emoji",
        "offset": utf16_length(full_text[:position]),
        "length": utf16_length(emoji),
        "custom_emoji_id": emoji_id,
    }


entities = [
    custom_emoji_entity(message, WOW_BEAR, WOW_BEAR_ID),
    custom_emoji_entity(message, BRIEFCASE_BEAR, BRIEFCASE_BEAR_ID),
    custom_emoji_entity(message, GLASSES_BEAR, GLASSES_BEAR_ID),
    custom_emoji_entity(message, THUMBSUP_BEAR, THUMBSUP_BEAR_ID),
]

response = requests.post(
    TELEGRAM_URL,
    data={
        "chat_id": CHAT_ID,
        "text": message,
        "entities": json.dumps(entities),
        "disable_web_page_preview": "false",
    },
    timeout=30,
)

print("========================================")
print("Telegram-Test: neue Angebote")
print("========================================")
print("Status:", response.status_code)
print(response.text)

if not response.ok:
    raise SystemExit("❌ Die Testnachricht konnte nicht gesendet werden.")

print()
print("✅ Vollständige Testnachricht wurde gesendet.")
