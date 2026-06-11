import pandas as pd
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

customers = pd.read_csv(os.path.join(base_dir, "data", "AdventureWorks_CustomerMaster.csv"), encoding="latin-1")
orders = pd.read_csv(os.path.join(base_dir, "data", "AdventureWorks_SalesOrderHeader.csv"), encoding="latin-1")
vendors = pd.read_csv(os.path.join(base_dir, "data", "AdventureWorks_VendorMaster.csv"), encoding="latin-1")

print("Files loaded successfully!")
print(customers.head())
# Check for missing values
print("\nMissing values:")
print(customers.isnull().sum())

# Check for duplicates
print("\nDuplicates:", customers.duplicated().sum())

# Clean
customers.drop_duplicates(inplace=True)
orders.drop_duplicates(inplace=True)
vendors.drop_duplicates(inplace=True)

customers.dropna(inplace=True)
orders.dropna(inplace=True)
vendors.dropna(inplace=True)

# Save cleaned files
customers.to_csv(os.path.join(base_dir, "data", "clean_customers.csv"), index=False)
orders.to_csv(os.path.join(base_dir, "data", "clean_orders.csv"), index=False)
vendors.to_csv(os.path.join(base_dir, "data", "clean_vendors.csv"), index=False)

print("\nCleaned files saved!")