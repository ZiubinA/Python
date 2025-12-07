import pandas as pd 

df = pd.read_csv("employees.csv")
df_copy = df.copy()
sorted_emloyees = df_copy.sort_values(by="performance_score", ascending=False)
print(sorted_emloyees.head(5))

juniors = df_copy[(df_copy["years_experience"] <= 2) & (df_copy["salary"] < 60000)]
print('\n', "juniors", juniors)

review_list = df_copy[(df_copy["performance_score"] < 3) | (df_copy["salary"] < 50000)]
print("\n Review needed \n", review_list)

non_eng = df_copy[~(df_copy["department"] == "Engineering")]

print("\n mean of salary non engineers", non_eng["salary"].mean())

depts = ["Marketing", "Sales"]
bonus_depts = df_copy[(df_copy["department"].isin(depts))]

#bonus_depts.insert(column="bonus_amount", value=bonus_depts["salary"] * 0.10, loc=0)
bonus_depts["bonus_amount"] = bonus_depts["salary"] * 0.10
print(bonus_depts)

print("\n bonused \n", bonus_depts)

middle_employees = df_copy[(df_copy["years_experience"] >=3) & (df_copy["years_experience"] < 7)]
print("\n middle employees", middle_employees)

legal_dep = df_copy[df_copy["department"] == "Legal"].sort_values(by="salary", ascending=False)
print(legal_dep)

excldep = ["Engineering","Legal"]
exclude_engineers = df_copy[~(df_copy["department"].isin(excldep))]
print("\n exluded enfineers \n", exclude_engineers)
taged_people = df_copy
taged_people["is_top_tier"] = df_copy["performance_score"] == 5

print("\n", taged_people)

underpaid_stuf = df_copy[(df_copy["salary"] < 75000) & (df_copy["years_experience"] > 4)]
underpaid_stuf_names = underpaid_stuf["name"]
print(underpaid_stuf_names)

   