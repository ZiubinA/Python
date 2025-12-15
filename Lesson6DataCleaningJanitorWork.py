import pandas as pd 
import numpy as np 

data = {
    "name": ["Jonas", "Petras", np.nan, "Darius"],
    "age": [30, np.nan, 25, 40],
    "salary": [2000, 1500, 1800, np.nan]
}
df = pd.DataFrame(data)

print(df)

print(df.isna().sum())#detecting Nan("missing data")

# 1. Drop row if ANY column has NaN
clean_df = df.dropna() 

# 2. Drop row only if ALL columns are NaN
clean_df = df.dropna(how='all')

# 3. Drop row if specific column is missing (Common)
# Example: If 'name' is missing, the record is useless.
clean_df = df.dropna(subset=['name'])

# 1. Fill with a static number (e.g., 0)
df["salary"] = df["salary"].fillna(0)

# 2. Fill with the Mean (Average) - Very Common for Age/Salary
mean_age = df["age"].mean()
df["age"] = df["age"].fillna(mean_age)

# 3. Fill with "Unknown" (for text)
df["name"] = df["name"].fillna("Unknown")

# Check types
print(df.dtypes)

# Convert 'age' to integer (after filling NaNs!)
df["age"] = df["age"].astype(int)

# Convert to float
df["salary"] = df["salary"].astype(float)

# 1. Check for duplicates (Returns True/False)
#print(df.duplicated().sum())

# 2. Drop duplicates (Keep the first occurrence)
#df = df.drop_duplicates()

# 3. Drop duplicates based on specific columns
# Example: If two rows have the same 'transaction_id', drop one.
#df = df.drop_duplicates(subset=["transaction_id"])

# Calculate the mean salary per role and fill NaNs in 'salary'
#df["salary"] = df["salary"].fillna(
#    df.groupby("role")["salary"].transform("mean")
#)

df = pd.read_csv("products_large.csv")
df_copy = df
#First Tasks
#print("\nmissing values\n", df_copy.isna().sum())
#clean_df = df_copy.dropna() 
#print('\n', clean_df, '\n')
#print("\nmissing values after cleaning\n", clean_df.isna().sum())
#filled_gaps = df_copy
#filled_gaps["stock"] = filled_gaps["stock"].fillna(0) 
#print("\n filled gaps in srock\n", filled_gaps)
#filled_gaps["price"] = filled_gaps["price"].astype(float)
#mean_price = filled_gaps["price"].mean()
#filled_gaps["price"] = filled_gaps["price"].fillna(mean_price)
#print("\n filled gaps in price\n", filled_gaps)

#SecondTasks
clean_df = df_copy
clean_df["price"] = clean_df["price"].str.replace("$", "").str.replace(",","")
clean_df["price"] = clean_df["price"].astype(float)
clean_df["product"] = clean_df["product"].str.title()
df["price"] = df["price"].fillna(df.groupby("category")["price"].transform("mean"))
clean_df = clean_df.drop_duplicates()
print("\n price converted to float", clean_df) 

role_avg = clean_df.groupby("category")["price"].transform("mean")
underpaid_filter = clean_df["price"] < (role_avg * 0.5)
underpaid_employees = clean_df[underpaid_filter]
print(underpaid_employees)


