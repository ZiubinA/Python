import pandas as pd

df_jan = pd.DataFrame({"id": [1, 2], "sales": [100, 200]})
df_feb = pd.DataFrame({"id": [3, 4], "sales": [150, 300]})

# Stack them vertically (axis=0 is default)
total_sales = pd.concat([df_jan, df_feb], ignore_index=True)

print(total_sales)

users = pd.DataFrame({
    "user_id": [1, 2, 3],
    "name": ["Jonas", "Petras", "Darius"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103],
    "user_id": [1, 1, 4], # Note: User 4 exists here but not in 'users' table!
    "amount": [50, 100, 25]
})

# SQL: SELECT * FROM users INNER JOIN orders ON users.user_id = orders.user_id
df_inner = pd.merge(users, orders, on="user_id", how="inner")

print(df_inner)
# User 1 (Jonas) is kept.
# User 2 (Petras) is dropped (no orders).
# User 3 (Darius) is dropped (no orders).
# Order for User 4 is dropped (user doesn't exist).

# SQL: SELECT * FROM users LEFT JOIN orders ...
df_left = pd.merge(users, orders, on="user_id", how="left")

print(df_left)
# Jonas: Has orders.
# Petras: amount = NaN (He exists, but bought nothing).

# Left table has 'id', Right table has 'user_id'
#df_merged = pd.merge(
#    users_with_id_col, 
#    orders, 
#    left_on="id", 
#    right_on="user_id", 
#    how="inner"
#)

print("\n Tasks\n")

import pandas as pd

products = pd.DataFrame({
    "prod_id": [101, 102, 103, 104],
    "prod_name": ["Laptop", "Mouse", "Monitor", "Printer"],
    "category": ["Tech", "Tech", "Tech", "Office"]
})

sales = pd.DataFrame({
    "sale_id": [1, 2, 3, 4, 5],
    "prod_id": [101, 101, 103, 105, 101], # Note: 105 is unknown product
    "amount": [1200, 1200, 300, 50, 1200]
})

df = pd.merge(sales, products, on ="prod_id", how="left")
print(df)

df = pd.merge(products, sales, on="prod_id", how="outer").reset_index()
unsold = df.groupby("prod_id").filter(lambda x: x["sale_id"].isna().any() | x["amount"].isna().any())
#faster way unsold = df[ (df["sale_id"].isna()) | df["amount"].isna()]
print("\n",unsold)

df = pd.merge(sales, products, on="prod_id", how="outer").reset_index()
print(df)
df = df.groupby("category")["amount"].sum().reset_index()
print(df)

new_sales = pd.DataFrame({
    "sale_id": [6], 
    "prod_id": [102], 
    "amount": [25]
})

sales = pd.concat([sales, new_sales], ignore_index=True)
print(sales)