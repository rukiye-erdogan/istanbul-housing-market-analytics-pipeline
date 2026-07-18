from pathlib import Path
import json
import os

import requests
from dotenv import load_dotenv

load_dotenv(Path(".env"))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

text = "🤩 💼 🤓 👍"

entities = [
    {
        "type": "custom_emoji",
        "offset": 0,
        "length": 2,
        "custom_emoji_id": "5224643461487044408"
    },
    {
        "type": "custom_emoji",
        "offset": 3,
        "length": 2,
        "custom_emoji_id": "5222357516683353476"
    },
    {
        "type": "custom_emoji",
        "offset": 6,
        "length": 2,
        "custom_emoji_id": "5224238334401876298"
    },
    {
        "type": "custom_emoji",
        "offset": 9,
        "length": 2,
        "custom_emoji_id": "5222122852555201410"
    }
]

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": text,
        "entities": json.dumps(entities)
    },
    timeout=30,
)

print("Status:", response.status_code)
print(response.text)
