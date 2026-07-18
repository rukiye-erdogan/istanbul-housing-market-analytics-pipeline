#!/usr/bin/env python3

from pathlib import Path
import subprocess
import sys
from datetime import datetime

PROJECT = Path.home() / "Documents/GitHub/istanbul-housing-market-analytics-pipeline"
LOG_DIR = PROJECT / "logs"
LOG_DIR.mkdir(exist_ok=True)

today = datetime.now().day

print("=" * 60)
print("LaunchAgent Pipeline")
print(datetime.now())
print("=" * 60)

if today % 2 != 0:
    print(f"Today is day {today}.")
    print("Skipping pipeline (only even calendar days).")
    sys.exit(0)

print("Even calendar day detected.")
print()

print("1. Starting scraper...")
subprocess.run(
    [sys.executable, "scripts/scraping/scrape_hepsiemlak.py"],
    cwd=PROJECT,
    check=True,
)

print()
print("2. Starting pipeline...")
subprocess.run(
    [sys.executable, "-m", "scripts.run_pipeline"],
    cwd=PROJECT,
    check=True,
)

print()
print("Finished successfully.")
