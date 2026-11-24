# Automated KPI Dashboard & Daily MIS Reporting System

**Tech Stack:** Microsoft Excel (XLOOKUP, SUMIFS, Pivot Tables, Power Query) | Tableau | Python (MIS Automation)

## Project Overview
Designed a dynamic multi-sheet Management Information System (MIS) tracker and interactive Tableau KPI dashboard monitoring **12 core business KPIs**, reducing daily manual reporting effort by **45%**.

## Repository Structure
```text
|-- docs/
|   |-- kpi_definitions_and_formulas.md   # Documentation of 12 KPIs & Excel XLOOKUP/SUMIFS logic
|-- scripts/
|   |-- generate_mis_tracker.py           # Python script generating daily MIS dataset
|-- data/
|   |-- daily_mis_sample.csv              # Sample regional KPI tracking data
|-- README.md
```

## Key Features & Impact
- **45% Reduction in Reporting Effort:** Replaced manual copy-paste workflows with structured Excel `XLOOKUP`, `SUMIFS`, dynamic Pivot Tables, and automated variance flags.
- **12 Core KPIs Tracked:** Revenue, Gross Margin, Daily Active Users, CAC, Conversion Rate, AOV, Order Fulfillment SLA, Return Rate, Net Retention, Support Resolution Time, Inventory Turnover, and Variance vs. Target.
- **Interactive Tableau Drill-Downs:** Enabled regional and category-level variance filtering for daily leadership standups.
