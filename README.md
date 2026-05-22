# Istanbul Housing Market Analytics Pipeline

**End-to-end Real Estate Analytics Pipeline**  
From Raw Data to Business Insights using Modern Data Engineering Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
[![Tableau](https://img.shields.io/badge/Tableau-Live%20Dashboard-orange?style=for-the-badge&logo=tableau&logoColor=white)](https://public.tableau.com/views/IstanbulHousingMarketAnalytics2026/IstanbulHousingMarketAnalytics2026)

## Live Dashboard

Interactive Tableau dashboards for exploring Istanbul housing market trends and analytics.

## Dashboard Previews

### Market Analytics Dashboard – Istanbul Housing Market Analytics 2026

![Istanbul Housing Market Analytics 2026](assets/dashboards/istanbul-housing-market-analytics-2026.png)

🔗 Tableau Dashboard:
https://public.tableau.com/views/IstanbulHousingMarketAnalytics2026/IstanbulHousingMarketAnalytics2026

---

### Residence Listings Dashboard – Istanbul Residence Listings Analysis

![Istanbul Residence Listings Analysis](assets/dashboards/istanbul-residence-listings-analysis.png)

🔗 Tableau Dashboard:
https://public.tableau.com/views/IstanbulResidenceListingsAnalysis/IstanbulResidenceListingsAnalysis

## Pipeline Architecture

<p align="center">
  <br>
  <br>
  <img src="assets/pipeline-architecture.png.drawio.png" width="400">
  <br>
  <br>
</p>
                                                                              
## Project Overview

This project analyzes the Istanbul housing market using an end-to-end data analytics pipeline built with Python, SQL, and Tableau.

The pipeline processes more than 24,000 housing listings and transforms raw real estate data into actionable business insights through data cleaning, exploratory analysis, and interactive dashboard visualization.

The project aims to identify:
- Pricing trends across Istanbul districts
- High-value investment opportunities
- Property distribution patterns
- Market segmentation insights

## Key Business Insights

```markdown
# Istanbul Housing Market Analytics 2026

## Overview
This dashboard provides a comprehensive analysis of Istanbul’s residential real estate market using interactive visualizations and district-based comparisons. The project focuses on identifying pricing trends, regional differences, housing characteristics, and investment insights across both the Asian and European sides of Istanbul.

---

# Key Insights

## District-Based Price Analysis
Significant price differences exist between Istanbul districts.

### Highest Average Prices per m²
- Bakırköy → ~777,143 ₺/m²
- Beşiktaş
- Sarıyer
- Kağıthane
- Bayrampaşa

### Lowest Average Prices per m²
- Esenyurt → ~35,363 ₺/m²

### Main Insight
Luxury and centrally located districts on the European side dominate the premium real estate market.

---

## Residential Complex Entry Prices
The dashboard also analyzes minimum entry prices for luxury residential complexes.

### Examples
- Beyaz Vadi Konakları Sitesi → ~98M ₺
- Naile Sultan Sitesi → ~265M ₺

### Main Insight
Luxury residential projects are heavily concentrated in premium districts such as Beşiktaş and nearby high-income areas.

---

## Asian vs European Side Comparison

### Average Price per m²
- Asian Side (Anatolian) → ~135,750 ₺/m²
- European Side (Thracian) → ~131,606 ₺/m²

### Main Insight
- The Asian side slightly outperforms the European side in average price per square meter.
- The European side contains a stronger concentration of ultra-luxury residential projects.

---

## Property Size Category Analysis

### Average Price per m² by Size
- Small (<80m²) → ~178,568 ₺
- Mid-sized (80–120m²) → ~113,000 ₺
- Large (121–200m²) → ~132,000 ₺
- Spacious (>200m²) → ~145,236 ₺

### Main Insight
- Smaller apartments achieve the highest price per square meter.
- Mid-sized apartments offer better price efficiency.
- Large luxury apartments regain value due to exclusivity and premium locations.

---

## Furnishing Status Impact

### Examples
- Furnished apartments in Küçükçekmece → ~71,050 ₺/m²
- Unfurnished apartments in Beylikdüzü → ~49,153 ₺/m²

### Main Insight
Furnished apartments generally achieve higher prices per square meter, although district location remains the strongest pricing factor.

---

## Building Age vs Price Relationship

### Average Price per m² by Building Age
New Build (0–5 years):
- Asian Side → ~159,742 ₺/m²
- European Side → ~155,680 ₺/m²

### Main Insight
- New developments command the highest market premiums.
- Older buildings show noticeably lower market values.
- Property age has a strong correlation with pricing.

---

# Dashboard Features
- Interactive district filtering
- Side-based comparison (Asian vs European)
- Residential complex analysis
- Dynamic tooltip insights
- Bubble charts, scatter plots, and bar charts
- Comparative real estate analytics

---

# Skills & Technologies
- Data Visualization
- Business Intelligence
- Real Estate Analytics
- Dashboard Design
- Comparative Market Analysis
- Interactive Reporting
- Data Storytelling

---

# Conclusion
The dashboard reveals substantial pricing disparities across Istanbul’s districts and highlights how factors such as location, property size, furnishing status, and building age significantly influence real estate prices. The analysis also demonstrates the dominance of luxury residential developments in premium districts and provides valuable insights for investors, analysts, and decision-makers.


# Istanbul Residence Listings Analysis

## Project Overview
Istanbul Residence Listings Analysis was developed as part of a mini data engineering and business intelligence pipeline project. The primary objective was to design a workflow capable of automatically collecting, processing, and visualizing real estate listing data from Istanbul.

The project was intended to simulate a real-world BI environment in which newly collected property data would continuously update the dashboard through an automated pipeline.

---

# Project Objective
The main goals of the project were:

- Automated collection of residence listing data
- Data cleaning and preprocessing
- Structured data storage
- Tableau dashboard integration
- Automated dashboard data refresh workflow

---

# Current Project Status
Istanbul Residence Listings Analysis currently includes the complete dashboard structure and analytical framework. Core visualizations and KPI logic have already been implemented, including:

- Residence listings by district
- Average property price analysis
- Time-based listing monitoring
- Interactive district filtering

The automation workflow, however, could not be fully finalized due to limitations of Tableau Public Web Authoring, which does not support advanced scheduling and automatic data refresh functionality.

---

# Technical Limitation
Since the project was built using Tableau Public Web Authoring, direct pipeline automation and scheduled refresh capabilities were limited.

In a production-ready environment using:
- Tableau Desktop
- Tableau Cloud
- Tableau Server
- External ETL orchestration tools (Python, APIs, Cron Jobs, Airflow, etc.)

the dashboard could be integrated into a fully automated end-to-end data pipeline.

---

# Planned Pipeline Architecture
The intended architecture included:

1. Automated scraping of residence listing data
2. Scheduled preprocessing and data cleaning
3. Automated dataset updates
4. Dynamic Tableau dashboard refresh
5. Continuous market trend monitoring

---

# Skills & Concepts Demonstrated
- Data Visualization
- Business Intelligence
- Tableau Dashboard Development
- ETL / ELT Pipeline Planning
- Real Estate Market Analysis
- Interactive Reporting
- Dashboard Architecture Design

---

# Future Improvements
Potential future enhancements include:

- Migration to Tableau Desktop or Tableau Cloud
- Automated Python ETL pipelines
- Scheduled refresh implementation
- Database integration
- Live API connections
- Expanded historical trend analysis

---

# Conclusion
Istanbul Residence Listings Analysis successfully establishes the foundation for a scalable and automated real estate analytics pipeline. While full automation could not be completed within Tableau Public Web Authoring, the project demonstrates the architecture, analytical logic, and workflow design required for a production-ready business intelligence solution.
```


## Project Structure

## 📂 Project Structure

```bash
istanbul-housing-market-analytics-pipeline/
├── assets/
│   ├── architecture/              # Pipeline architecture diagrams
│   ├── bot/                       # Telegram bot assets & visuals
│   ├── branding/                  # Branding elements & custom graphics
│   ├── dashboards/                # Tableau dashboard screenshots
│   └── screenshots/               # Additional project visuals
│
├── dashboards/                    # Tableau dashboard workbooks
│
├── data/
│   ├── raw/                       # Raw scraped datasets
│   ├── processed/                 # Cleaned & transformed datasets
│   ├── historical/                # Historical residence price tracking
│   ├── snapshots/                 # Daily pipeline snapshots
│   ├── istanbul_housing.db        # SQLite database
│   └── CSV exports                # Pipeline output datasets                   
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── 02_big_data_architecture.ipynb
│
├── scripts/
│   ├── alerts/                    # Telegram notification logic
│   ├── automation/                # Automated scheduling scripts
│   ├── processing/
│   │   └── exchange_rates.py      # Currency conversion logic
│   ├── scraping/
│   │   └── scrape_hepsiemlak.py   # Istanbul residence web scraping
│   └── run_pipeline.py            # Main ETL pipeline execution
│
├── tests/
│   └── test_connection.py
│
├── presentation/                  # Final project presentation
├── run_full_pipeline.sh           # Full automation runner
├── requirements.txt               # Python dependencies
├── README.md
└── LICENSE
```

## 🤖 Automated Telegram Alert System

The project includes an automated Telegram bot that continuously monitors residence listings across Istanbul.

Every two days, the pipeline automatically executes the complete ETL workflow:

1. Scrapes new residence listings from Istanbul-based real estate platforms  
2. Cleans and processes the incoming housing data  
3. Tracks newly added properties and market changes  
4. Converts all property prices into:
   - Turkish Lira (₺)
   - Euro (€)
   - US Dollar ($)
5. Sends automated Telegram notifications with the latest market updates

This automation creates a lightweight real-estate monitoring system for tracking Istanbul's residence market in near real-time.

### Key Features

- Automated scraping every 48 hours
- Istanbul-focused residence monitoring
- Multi-currency price conversion
- Automated Telegram alerts
- Historical snapshot tracking
- Scalable ETL architecture
- Fully automated pipeline execution

---

## 📲 Telegram Bot Integration

The project includes a fully automated Telegram notification system called:

### Istanbul Housing Alerts Bot

The bot was designed as a lightweight real-estate monitoring assistant focused exclusively on residence listings in Istanbul.

Users automatically receive curated housing alerts, market updates, and filtered residence opportunities directly through Telegram.

---

### 🔄 Automated Workflow

Every 48 hours, the system automatically:

- Scrapes new Istanbul residence listings
- Detects newly added offers
- Filters relevant housing opportunities
- Processes and cleans the data
- Converts listing prices into:
  - Turkish Lira (₺)
  - Euro (€)
  - US Dollar ($)
- Sends personalized Telegram notifications

---

### 🧠 Smart Notification Logic

The bot distinguishes between:

- New residence opportunities
- No-change market updates
- Historical market tracking
- Automated monitoring cycles

This creates a clean user experience without unnecessary spam notifications.

---

### 🎨 Bot Branding & UX Design

The Telegram bot includes a custom-designed visual identity featuring:

- Personalized mascot branding
- Emotion-based Telegram reactions
- Friendly conversational tone
- Real-estate focused storytelling
- Istanbul-themed visuals
- Automated market assistant behavior

The goal was to combine data engineering with a user-friendly product experience.

---

## 📸 Telegram Bot Preview

### 🐻 Istanbul Housing Alerts Bot

Custom-designed Telegram assistant for automated Istanbul residence monitoring.

<p align="center">
  <img src="assets/bot/bot_profile.png" width="240"/>
</p>

---

### 🎨 Bot Branding & Workflow

<p align="center">
  <img src="assets/bot/telegram_bot_branding.png" width="950"/>
</p>

---

### 📩 New Residence Alert

The bot automatically sends notifications whenever new Istanbul residence listings are detected during the scheduled scraping cycle.

<p align="center">
  <img src="assets/bot/telegram_new_listing.png" width="520"/>
</p>

---

### 📊 No-New-Listing Notification

If no new residence opportunities are found, the bot sends a friendly market monitoring update instead of unnecessary spam notifications.

<p align="center">
  <img src="assets/bot/telegram_no_new_listing.png" width="520"/>
</p>

---

### 🐻 Custom Emoji System

The Telegram assistant includes custom-designed mascot reactions to create a more engaging and user-friendly experience.

<p align="center">
  <img src="assets/screenshots/daumenhoch_1_EMOJI.png" width="80"/>
  <img src="assets/screenshots/peace_4_EMOJI.png" width="80"/>
  <img src="assets/screenshots/schlaubi_2_EMOJI.png" width="80"/>
  <img src="assets/screenshots/woaw_3_EMOJI.png" width="80"/>
</p>

---
