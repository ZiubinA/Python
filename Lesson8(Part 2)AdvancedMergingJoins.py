import pandas as pd
import numpy as np
employees = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Jonas", "Petras", "Darius", "Ruta"],
    "manager_id": [None, 1, 1, 2] # Petras(2) reports to Jonas(1)
})

# We join the table to itself!
# Left Side = Employee (Use manager_id)
# Right Side = Manager (Use emp_id)
df_hierarchy = pd.merge(
    employees, 
    employees, 
    left_on="manager_id", 
    right_on="emp_id", 
    how="left",
    suffixes=("_emp", "_mgr") # Rename columns to avoid collision
)

# Result will have 'name_emp' (Petras) and 'name_mgr' (Jonas)
print(df_hierarchy)

months = pd.DataFrame({"month": ["Jan", "Feb", "Mar"]})
products = pd.DataFrame({"product": ["A", "B"]})

# how="cross" (New in Pandas 1.2+)
template = pd.merge(months, products, how="cross")
print(template)

#df_diff = pd.merge(table_A, table_B, on="id", how="outer", indicator=True)
# Filter for items ONLY in table B
#new_items = df_diff[ df_diff["_merge"] == "right_only" ]

print("\n Tasks \n")

# Employee Table
employees = pd.DataFrame({
    "id": [10, 20, 30, 40, 50],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "manager_id": [None, 10, 10, 20, 20] 
})

# Systems Data (for comparison)
legacy_system = pd.DataFrame({"user": ["Alice", "Bob", "Charlie"]})
new_system = pd.DataFrame({"user": ["Bob", "Charlie", "David", "Eve"]})

# Inventory Data
colors = pd.DataFrame({"color": ["Red", "Blue"]})
sizes = pd.DataFrame({"size": ["S", "M", "L"]})

df = pd.merge(
    employees,
    employees,
    left_on="manager_id",
    right_on="id",
    how="left",
    suffixes=("_emp", "_mgr"))


#result = df.columns("name_emp", "manager_id_mgr")
print(df)

#print(result)
df = pd.merge(new_system, legacy_system, on="user", how="left")
print(df)
df = pd.merge(legacy_system, new_system, on="user", how="outer", indicator=True)
print(df)

missing_users = df[df["_merge"] == "left_only"]


new_adds = df[df["_merge"] == "right_only"]

print("\n--- Missing in New System (Lost Users) ---")
print(missing_users)

print("\n--- New Adds (New Users) ---")
print(new_adds)


#inventory = pd.merge(colors, sizes, how="cross")
#
#inventory["sku"] = inventory["color"] + "-" + inventory["size"]
#
#print("\nFull Inventory List")
#print(inventory)
#
#
#is_manager = employees["emp_id"].isin(employees["manager_id"])
#managers = employees[is_manager]
#
#print("\nManagers Found")
#print(managers)

#managers_merge = pd.merge(
#    employees, 
#    employees[["manager_id"]].drop_duplicates(), 
#    left_on="emp_id", 
#    right_on="manager_id", 
#    how="inner" 
#)
#
#print("\nManagers Found")
##print(managers_merge[["emp_id", "name"]])

jan_subs = pd.DataFrame({
    "user_id": [101, 102, 103, 104, 105],
    "email": ["alice@mail.com", "bob@mail.com", "charlie@mail.com", "dave@mail.com", "eve@mail.com"]
})

feb_subs = pd.DataFrame({
    "user_id": [101, 103, 105, 106], # 102 (Bob) and 104 (Dave) are missing!
    "status": ["Active", "Active", "Active", "New"]
})

df = pd.merge(jan_subs, feb_subs, on="user_id", how="outer", indicator=True)
print("\n jav feb subs\n", df)
usrJan = df[df["_merge"] == "left_only"]
print("\nusers in left table only\n", usrJan["email"])

mains = pd.DataFrame({"dish": ["Burger", "Pizza", "Salad"]})
drinks = pd.DataFrame({"drink": ["Coke", "Water", "Juice"]})

menu = pd.merge(mains, drinks, how="cross")
print(menu)

menu["combo_name"] = menu["dish"] + '-' + menu["drink"]
print(menu)

menu["price"] = np.where(menu["combo_name"] == "Pizza-Coke", 10, 12)

print(menu)

follows = pd.DataFrame({
    "follower": ["A", "B", "C", "D", "E", "F"],
    "followee": ["B", "C", "B", "B", "C", "A"] 
})
popular = follows.groupby("followee").filter(lambda x: len(x) >= 2)
print(popular)