import pandas as pd
import numpy as np

np.random.seed(101)
dates = pd.date_range("2026-01-01", periods=90, freq="D")
regions = ["North", "South", "East", "West"]

rows = []
for d in dates:
    for r in regions:
        target = np.random.randint(180000, 250000)
        actual = int(target * np.random.uniform(0.85, 1.15))
        orders = np.random.randint(120, 260)
        rows.append([d.strftime("%Y-%m-%d"), r, target, actual, orders, round(actual / orders, 2)])

df = pd.DataFrame(rows, columns=["Date", "Region", "Target_Revenue", "Actual_Revenue", "Total_Orders", "AOV"])
df["Variance_Pct"] = ((df["Actual_Revenue"] - df["Target_Revenue"]) / df["Target_Revenue"] * 100).round(2)
df.to_csv("data/daily_mis_sample.csv", index=False)
