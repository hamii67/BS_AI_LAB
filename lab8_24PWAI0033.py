   



import os

print("Current Folder:", os.getcwd())
print("Files:", os.listdir("E:/BS_AI_LAB"))
import pandas as pd

# Load data
customers = pd.read_csv("customers.csv")
purchases = pd.read_csv("purchases.csv")
membership = pd.read_csv("membership.csv")

# Data Preview
print(customers.head())
print(customers.shape)

# Handle Missing Values
customers["Age"] = customers["Age"].fillna(customers["Age"].median())
customers["Income"] = customers["Income"].fillna(customers["Income"].mean())
customers["City"] = customers["City"].fillna("Unknown")
purchases["Amount"] = purchases["Amount"].fillna(purchases["Amount"].median())

# Remove Duplicates
customers.drop_duplicates(inplace=True)
purchases.drop_duplicates(inplace=True)

# Standardize Data
customers["City"] = customers["City"].str.title()
customers["Gender"] = customers["Gender"].str.upper()

# Merge Data
data = pd.merge(customers, purchases, on="CustomerID", how="left")
data = pd.merge(data, membership, on="CustomerID", how="left")

# Feature Engineering
data["AgeGroup"] = data["Age"].apply(
    lambda x: "Young" if x <= 30 else "Adult" if x <= 50 else "Senior"
)

data["SpendingScore"] = data["Amount"] * data["Quantity"]

# Save Final Dataset
data.to_csv("AI_Ready_Customers.csv", index=False)

# Analysis
print("Customers with Income > 80000")
print(customers[customers["Income"] > 80000])

print("Average Income by City")
print(customers.groupby("City")["Income"].mean())

print("Top Spending Customers")
print(data.sort_values("SpendingScore", ascending=False).head(10))

print("Most Popular Product")
print(purchases["Product"].value_counts().idxmax())