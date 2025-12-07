import pandas as pd

s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s["a"]) # 10


data = {
    "name": ["Jonas", "Petras", "Darius"],
    "age": [30, 25, 40],
    "city": ["Kaunas", "Vilnius", "Klaipeda"]
}

df = pd.DataFrame(data)
print(df,'\n')

names = df["name"]
print(names,'\n')

df = df.set_index("name")

# Select row for "Jonas" (Label)
print(df.loc["Jonas"],'\n') 

# Select the 1st row (Position 0)
print(df.iloc[0])

# Syntax: df[ condition ]

# 1. Who is older than 25?
adults = df[ df["age"] > 25 ]

# 2. Multiple conditions (Use & for AND, | for OR)
# Note: Parentheses () are MANDATORY in Pandas!
target = df[ (df["age"] > 25) & (df["city"] == "Kaunas") ]

print("5. Practical Assignment (Homework)")

df = pd.read_csv("pandasPracticeTasksdata.csv")

shape = df.shape
print("Shape:", shape)
average = df['price'].mean()
print("Mean:", average)
expensive_electronics = df[(df["category"] == "Electronics") & (df["price"] > 500)] 
print(expensive_electronics)

total_value = df["price"] * df["stock"]

print(total_value)

df = df.set_index('product')
print(df.loc["Monitor"])

df = pd.read_csv("pandasPracticeTasksdata.csv")
warnings = df[(df["stock"] < 10) | (df["price"] > 1000)]
print('\n', warnings)

target_cats = ["Electronics", "Accessories"]
filtered = df[(df["category"].isin(target_cats))]
print('\n', filtered)

discounted_price = filtered["price"] * 0.9
print('\n', discounted_price)

revenue_potential = df["price"] * df["stock"]
revenue_fir3 = revenue_potential.head(3)
sorted_revenue = revenue_potential.sort_values()
print('\n', "Sorted Revenue", sorted_revenue, '\n')
print(revenue_fir3, '\n')

phones = df[(df["product"] == "Phone")]
price = phones["price"].values[0]
print("price of the phone", price)
