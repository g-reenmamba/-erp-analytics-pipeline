import pandas as pd
import os

# Get the base project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load clean orders data
orders = pd.read_csv(os.path.join(base_dir, "data", "clean_orders.csv"))

# Convert date column
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["Month"] = orders["OrderDate"].dt.to_period("M")

# Total Revenue
total_revenue = orders["TotalDue"].sum()
print(f"Total Revenue: ${total_revenue:,.2f}")

# Top 10 Customers by Revenue
top_customers = orders.groupby("CustomerID")["TotalDue"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Revenue:")
print(top_customers)

# Monthly Revenue
monthly_revenue = orders.groupby("Month")["TotalDue"].sum()
print("\nMonthly Revenue:")
print(monthly_revenue)

# Save results
top_customers.to_csv(os.path.join(base_dir, "data", "top_customers.csv"))
monthly_revenue.to_csv(os.path.join(base_dir, "data", "monthly_revenue.csv"))

print("\nAnalysis saved!")