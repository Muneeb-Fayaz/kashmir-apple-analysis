# Kashmir Apple Market Analysis

An intermediate-level Python data-analysis project exploring apple production, mandi prices, arrivals/supply, demand indicators, and farmer profitability in Jammu & Kashmir using NumPy and Pandas.

## Data integrity
- `apple_production_official_2024_25.csv` contains district-wise Kashmir Division apple production transcribed from the Government of J&K, Directorate of Economics & Statistics, *Regional Digest of Statistics 2024-25*, Table 5.03 (concluded), values in thousand metric tonnes.
- Files ending in `_sample.csv` are **synthetic practice data**, not actual market observations. They are included so the project can be developed before downloading and cleaning real mandi records.
- Do not combine official and synthetic records as if they share the same provenance.

## Official sources
- J&K Directorate of Economics & Statistics: https://ecostatjk.nic.in/showdata.aspx?q=Regional_Digest_Stat
- Regional Digest of Statistics 2024-25 PDF: https://www.ecostatjk.nic.in/pdf/publications/regdigest/Regional%20Digest%202024-25.pdf
- AGMARKNET / OGD daily mandi price catalog: https://data.gov.in/catalog/current-daily-price-various-commodities-various-markets-mandi
- e-NAM AGMARKNET price dashboard: https://www.enam.gov.in/web/dashboard/agmarknet

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python src/day1_inspect_data.py
```

## Current scope
Day 1: project setup, data provenance, CSV loading, and initial inspection.
Later stages: data cleaning, production analysis, price analysis, supply-arrival analysis, demand proxies, profitability, and terminal reports.

## Units
Production is in thousand metric tonnes (000 MT). Mandi prices should be recorded in the exact unit supplied by the source (often INR per quintal); never compare prices until units and dates are standardized.

## Disclaimer
This is an educational analysis project, not an official price advisory or agricultural forecast.
