#!/bin/bash

echo "Starting Full Istanbul Housing Pipeline..."

# Zum Projektordner wechseln
cd ~/Documents/GitHub/istanbul-housing-market-analytics-pipeline

# Scraper starten
cd pipeline
python scrape_hepsiemlak.py

# Pipeline starten
cd ../scripts
python run_pipeline.py

echo "Pipeline Finished!"
