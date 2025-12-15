import pandas as pd
import json

# A JSON string simulating an API response
json_data = """
[
    {"session_id": 101, "user": "Sarah", "duration_sec": 120, "device": "Mobile"},
    {"session_id": 102, "user": "Mike", "duration_sec": null, "device": "Desktop"},
    {"session_id": 103, "user": null, "duration_sec": 45, "device": "Mobile"},
    {"session_id": 101, "user": "Sarah", "duration_sec": 120, "device": "Mobile"}, 
    {"session_id": 104, "user": "Tom", "duration_sec": 200, "device": null}
]
"""

df = pd.read_json(json_data)

df = df.dropna(subset=["user"])

df["duration_sec"] = df["duration_sec"].fillna(df.groupby("device")["duration_sec"].transform("mean"))
print(df)

sales_json = """
[
    {"id": 1, "product": "Laptop", "price": "$1200", "status": "Sold"},
    {"id": 2, "product": "Mouse", "price": "$25", "status": "Returned"},
    {"id": 3, "product": "Laptop", "price": null, "status": "Sold"},
    {"id": 1, "product": "Laptop", "price": "$1200", "status": "Sold"},
    {"id": 4, "product": null, "price": "$50", "status": "Sold"},
    {"id": 5, "product": "Monitor", "price": "$300", "status": null},
    {"id": 6, "product": "Mouse", "price": "$25", "status": "sold"}
]
"""

df = pd.read_json(sales_json)

df = df.dropna(subset=["product"])
print(df)

df["price"] = df["price"].str.replace("$", "")
df["price"] = df["price"].astype(float)
print(df)

df["status"] = df["status"].str.title()
print("\n", df)

df["status"] = df["status"].fillna("Unknown")
print("\n", df)

df = df.drop_duplicates()
print("\n", df)

df["price"] = df["price"].fillna(df.groupby("product")["price"].transform("mean"))
print("\n",df)

import pandas as pd
import numpy as np

data = {
    "id": [101, 102, 103, 101, 104, 105], # Note: 101 is duplicated
    "name": ["  Jonas ", "Petras", "Darius", "  Jonas ", "Antanas", "Ruta"],
    "role": ["Dev", "Manager", "Dev", "Dev", "Manager", "Intern"],
    "salary": ["$2,000", "$4,000", np.nan, "$2,000", np.nan, "$800"]
}

df = pd.DataFrame(data)

df = df.drop_duplicates()

df["salary"] = df["salary"].str.replace("$", "").str.replace(",", "")
df["salary"] = df["salary"].astype(float)
df["name"] = df["name"].str.strip().str.title()
df["salary"] = df["salary"].fillna(df.groupby("role")["salary"].transform("mean"))
print("\n", df)