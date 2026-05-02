import pandas as pd

# Load datasets
accounts = pd.read_csv("accounts.csv")
products = pd.read_csv("products.csv")
sales = pd.read_csv("sales_pipeline.csv")

# Basic cleaning
sales = sales.dropna()

# Join datasets
merged = sales.merge(products, on="product_id", how="left")

# Aggregation
summary = merged.groupby("product_name")["revenue"].sum().reset_index()

# Save output
summary.to_csv("output_summary.csv", index=False)

print("ETL Process Completed")
