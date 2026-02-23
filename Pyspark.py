import pandas as pd
import numpy as np

# A messy extract from the sales system
data = {
    'Date': ['2024-01-15', '2024-01-16', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20'],
    'Region': ['North', 'South', np.nan, 'North', 'South', 'East', 'North'], # Missing Region
    'Sales_Rep': ['Alex', 'Sarah', 'Alex', 'Mike', 'Sarah', 'Alex', 'Mike'],
    'Revenue': ['$1,200', '$850', '$1,200', '$500', '$900', '$1,100', '$500'], # Messy Currency (comma + $)
    'Cost': ['800', '400', '800', '200', '450', '600', '200'], # Numbers stored as Text
    'Status': ['Confirmed', 'Confirmed', 'Returned', 'Confirmed', 'Cancelled', 'Confirmed', 'Confirmed']
}

df = pd.DataFrame(data)
print("--- RAW DATA ---")
print(df)

dc = df.copy()
dc["Revenue"] = df["Revenue"].str.replace("$", "").str.replace(",", "").astype(float)
dc["Cost"] = dc["Cost"].astype(float)
dc["Region"] = dc["Region"].fillna("Global")

dc["Profit"] = dc["Revenue"] - dc["Cost"]
dc_filtered = dc[dc["Status"] == "Confirmed"]
print(dc_filtered)

report = dc_filtered.groupby(["Region", "Sales_Rep"]).agg(
    {
        "Revenue" : "sum",
        "Profit" : "sum"
    })

report = report.rename(columns=({
    "Revenue" : "Total_Sales",
    "Profit" : "Total_Profit"
}))
report = report.sort_values(by="Total_Profit", ascending=False)
print(report)