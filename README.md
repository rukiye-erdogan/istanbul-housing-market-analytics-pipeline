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
```


## Project Structure

```bash
istanbul-housing-market-analytics-pipeline/
├── data/              # Raw and processed datasets
├── 02_notebooks/         # Jupyter Notebooks (Exploration & Analysis)
├── scripts/           # Python Scripts (ETL, Processing)
├── dashboards/        # Tableau Workbooks
├── assets/            # Screenshots & Visuals
├── presentation/      # Abschlusspräsentation
├── requirements.txt      # Python Dependencies
└── README.md
