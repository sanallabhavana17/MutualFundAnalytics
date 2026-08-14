# Mutual Fund Analytics Internship

**Name:** Sanalla Bhavana

## Project Overview

This project focuses on analyzing mutual fund data using Python, SQL, and Power BI.

The project covers data ingestion, data cleaning, exploratory data analysis, performance analytics, advanced risk analysis, investor behaviour analysis, fund recommendation, and interactive dashboard development.

## Completed Tasks

### Day 1 — Data Ingestion & Setup

- Project folder structure created
- Git repository initialized
- Dependencies installed
- 10 datasets loaded using Pandas
- Live NAV data fetched from MFAPI
- NAV data saved as CSV
- Key mutual fund NAV data fetched
- Fund master analysis performed
- AMFI codes validated
- `requirements.txt` created

### Week 1 — Data Analytics Foundation

- NAV History dataset cleaned
- Investor Transactions dataset cleaned
- Scheme Performance dataset cleaned
- SQLite database created
- Database tables created
- Cleaned datasets imported into SQLite
- SQL queries written and executed
- Exploratory Data Analysis performed
- EDA report prepared
- Power BI dashboard created

### Advanced Analytics

- Daily return calculation
- Historical VaR at 95% confidence level
- CVaR calculation
- 90-day rolling Sharpe Ratio
- Investor cohort analysis
- SIP continuity analysis
- Fund recommendation scoring
- HHI category concentration analysis
- Advanced analytics charts created
- Advanced analytics findings documented

## Power BI Dashboard

The interactive Power BI dashboard contains:

- Executive Overview
- Fund Performance
- Investor Analytics
- SIP & Market Trends
- NAV Detail drill-through

### Dashboard Features

- Fund performance comparison
- NAV analysis
- Investor transaction analysis
- SIP behaviour analysis
- Risk and performance KPIs
- Date and fund filters
- Drill-through from Fund Performance to NAV Detail
- Interactive charts and cards

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Power BI
- Microsoft Excel
- Jupyter Notebook
- Visual Studio Code

## Project Structure

```text
MutualFund Analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
│
├── sql/
│   └── queries.sql
│
├── database/
│
├── dashboard/
│
├── reports/
│
├── clean_nav_history.py
├── clean_transactions.py
├── clean_scheme_performance.py
├── create_database.py
├── create_tables.py
├── import_data.py
├── run_queries.py
├── eda_analysis.py
├── requirements.txt
└── README.md