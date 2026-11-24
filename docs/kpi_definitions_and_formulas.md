# 12 Core KPIs & Excel Automation Logic

| # | KPI Name | Formula / Logic | Excel Implementation |
|---|---|---|---|
| 1 | Daily Revenue | `SUM(Net_Sales)` | `SUMIFS` by Date & Region |
| 2 | Target Variance % | `(Actual - Target) / Target` | Conditional Formatting (< -5% Red) |
| 3 | Gross Margin % | `(Revenue - COGS) / Revenue` | Calculated Field in Pivot Table |
| 4 | Average Order Value | `Total_Revenue / Total_Orders` | `IFERROR` + Dynamic Range |
| 5 | Conversion Rate | `Orders / Total_Sessions` | Funnel Summary Sheet |
| 6 | Customer Acquisition Cost | `Marketing_Spend / New_Customers` | `XLOOKUP` from Ad Spend Tab |
| 7 | Order Fulfillment SLA % | `On_Time_Orders / Total_Orders` | `COUNTIFS` SLA Tracker |
| 8 | Return / Refund Rate | `Returned_Units / Sold_Units` | Category Drill-Down Table |
| 9 | Repeat Purchase Rate | `Repeat_Buyers / Total_Buyers` | Cohort Lookup Matrix |
| 10 | Avg Resolution Time (Hrs) | `AVERAGE(Closed_Time - Open_Time)` | Support MIS Tab |
| 11 | Stockout Rate % | `Out_of_Stock_SKUs / Active_SKUs` | Inventory Alert Formula |
| 12 | Net Revenue Retention | `(Start_MRR + Expansion - Churn) / Start_MRR` | Executive Summary Card |
