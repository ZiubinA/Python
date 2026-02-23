import pandas as pd

df = pd.read_csv("heart.csv")
averageAge = df["age"].agg("mean")
print("Average Age:", averageAge)

print(df)

ds = df.copy()
ds = ds[ds["trestbps"] > 160]
print(ds)