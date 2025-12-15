import pandas as pd

data = {
    "store": ["Kaunas", "Vilnius", "Kaunas", "Vilnius", "Klaipeda"],
    "product": ["Apple", "Apple", "Banana", "Banana", "Apple"],
    "sales": [100, 150, 50, 60, 90],
    "quantity": [10, 15, 5, 6, 9]
}
df = pd.DataFrame(data)

# Question: What is the total sales per store?
# SQL: SELECT store, SUM(sales) FROM table GROUP BY store;

total_sales = df.groupby("store")["sales"].sum()

print(total_sales)
# store
# Kaunas      150  (100 + 50)
# Klaipeda     90
# Vilnius     210  (150 + 60)

# Question: How many items were sold per Store AND per Product?

output = df.groupby(["store", "product"])["quantity"].sum()

print(output)
# store     product
# Kaunas    Apple      10
#           Banana      5
# Klaipeda  Apple       9
# Vilnius   Apple      15
#           Banana      6

# Question: Get the Total Sales AND the Average Quantity per store.

stats = df.groupby("store").agg({
    "sales": "sum",      # Calculate Sum for Sales
    "quantity": "mean"   # Calculate Average for Quantity
})

print(stats)

# Get Min, Max, and Average Sales per Store
sales_stats = df.groupby("store")["sales"].agg(["min", "max", "mean"])

# Returns a Series (hard to use)
s = df.groupby("store")["sales"].sum()

# Returns a Clean DataFrame (easy to use)
df_new = df.groupby("store")["sales"].sum().reset_index()

data = {
    "department": ["IT", "HR", "IT", "Sales", "Sales", "HR", "IT"],
    "employee": ["Jonas", "Petras", "Darius", "Ruta", "Antanas", "Egle", "Mantas"],
    "salary": [2000, 1500, 2200, 1800, 1900, 1600, 3000],
    "years_exp": [2, 5, 3, 1, 2, 6, 10]
}

df = pd.DataFrame(data)

avgSaleDep = df.groupby("department")["salary"].mean().reset_index()
print("\n", avgSaleDep)
maxExpDep = df.groupby("department")["years_exp"].max().reset_index()
print(maxExpDep)
stats = df.groupby("department").agg({
    "employee" : "count",
    "salary" : ["min", "max"]
})
print(stats)
departmentIT = ["IT"]
filteredIT = df[(df["department"].isin(departmentIT))]
avgIT1 = filteredIT["salary"].mean()
print(avgIT1)

# Standard filtering checks rows.
# .filter() checks the GROUP.
# Logic: "Keep this group IF len(group) > 2"
big_depts = df.groupby("department").filter(lambda x: len(x) > 2)

# Rows = Department, Cols = Experience Level, Values = Average Salary
pivot = df.pivot_table(
    index="department", 
    columns="years_exp", 
    values="salary", 
    aggfunc="mean"
)

print(pivot)

# 1. Calculate sum per department and broadcast it back to every row
df["dept_total_salary"] = df.groupby("department")["salary"].transform("sum")

# 2. Calculate percentage
df["share_of_budget"] = df["salary"] / df["dept_total_salary"]

print("\n", df)

import pandas as pd
import numpy as np

data = {
    "team": ["Alpha", "Alpha", "Beta", "Beta", "Gamma", "Gamma", "Gamma"],
    "player": ["Jonas", "Petras", "Darius", "Ruta", "Antanas", "Egle", "Mantas"],
    "points": [10, 30, 20, 40, 5, 15, 10],
    "games_played": [2, 5, 3, 6, 1, 2, 2]
}
df = pd.DataFrame(data)

eliteTeam = df.groupby("team").filter(lambda x: x["points"].mean() > 15)

print("\nNew Task\n")
print(eliteTeam)
teamTotal = df.groupby("team")["points"].transform("sum")
df["contrubution"] = (df["points"] / teamTotal) * 100
print("\n", df)

pivot = df.pivot_table(
    index="team", 
    values="points", 
    aggfunc="max"
)

print(pivot)
def spread(x): return x.max() - x.min()
summery = df.groupby("team").agg({
    "games_played" : "sum",
    "points" : spread


    })

print(summery)

import pandas as pd

data = {
    "genre": ["Action", "Comedy", "Action", "Drama", "Comedy", "Drama", "Action"],
    "director": ["Nolan", "Waititi", "Bay", "Gerwig", "Waititi", "Nolan", "Bay"],
    "rating": [9.0, 8.2, 6.5, 8.8, 7.9, 9.2, 5.5],
    "budget_m": [200, 20, 150, 40, 25, 100, 200]
}
df = pd.DataFrame(data)

task1 = df.groupby("genre").agg({
    "rating" : "mean",
    "budget_m" : "sum"
}).sort_values(by="rating", ascending=False).reset_index()

print("\n",task1)

bigBudget = df.groupby("genre").filter(lambda x: x["budget_m"].sum() > 200)
print(bigBudget)

pivot = df.pivot_table(
    index="genre", 
    columns="director", 
    values="budget_m", 
    aggfunc="sum"
)

print(pivot)