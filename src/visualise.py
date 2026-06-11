import pandas as pd
import matplotlib.pyplot as plt
import os

# Get base project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load results from analysis
top_customers = pd.read_csv(os.path.join(base_dir, "data", "top_customers.csv"))
monthly_revenue = pd.read_csv(os.path.join(base_dir, "data", "monthly_revenue.csv"))

# --- Chart 1: Monthly Revenue Trend ---
plt.figure(figsize=(12, 5))
plt.plot(monthly_revenue["Month"], monthly_revenue["TotalDue"], marker="o", color="steelblue")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(base_dir, "data", "monthly_revenue_chart.png"))
plt.close()
print("Chart 1 saved!")

# --- Chart 2: Top 10 Customers by Revenue ---
plt.figure(figsize=(10, 6))
plt.barh(top_customers["CustomerID"].astype(str), top_customers["TotalDue"], color="coral")
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Total Revenue ($)")
plt.ylabel("Customer ID")
plt.tight_layout()
plt.savefig(os.path.join(base_dir, "data", "top_customers_chart.png"))
plt.close()
print("Chart 2 saved!")

print("\nAll charts saved to data folder!")