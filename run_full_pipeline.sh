#!/bin/bash

set -euo pipefail

PROJECT_DIR="$HOME/Documents/GitHub/istanbul-housing-market-analytics-pipeline"
LOG_DIR="$PROJECT_DIR/logs"
LOG_FILE="$LOG_DIR/pipeline_$(date '+%Y-%m-%d_%H-%M-%S').log"

mkdir -p "$LOG_DIR"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "========================================"
echo "Starting Full Istanbul Housing Pipeline"
echo "Date: $(date)"
echo "Project: $PROJECT_DIR"
echo "========================================"

cd "$PROJECT_DIR"

echo
echo "1. Starting Hepsiemlak scraper..."
python3 scripts/scraping/scrape_hepsiemlak.py

echo
echo "2. Starting processing and Telegram alerts..."
python3 -m scripts.run_pipeline

echo
echo "========================================"
echo "Pipeline finished successfully."
echo "Log: $LOG_FILE"
echo "========================================"
