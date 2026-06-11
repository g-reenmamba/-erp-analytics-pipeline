import pandas as pd
import os

# Get base project directory
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load data
orders = pd.read_csv(os.path.join(base_dir, "data", "clean_orders.csv"))
monthly_revenue = pd.read_csv(os.path.join(base_dir, "data", "monthly_revenue.csv"))
top_customers = pd.read_csv(os.path.join(base_dir, "data", "top_customers.csv"))

# Convert date
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])

# --- Calculations ---
total_revenue = orders["TotalDue"].sum()
total_orders = len(orders)
avg_order_value = orders["TotalDue"].mean()
best_month = monthly_revenue.loc[monthly_revenue["TotalDue"].idxmax(), "Month"]
best_month_revenue = monthly_revenue["TotalDue"].max()
top_customer_id = top_customers.iloc[0]["CustomerID"]
top_customer_revenue = top_customers.iloc[0]["TotalDue"]
date_from = orders["OrderDate"].min().strftime("%d %b %Y")
date_to = orders["OrderDate"].max().strftime("%d %b %Y")

# --- Print Report ---
print("=" * 45)
print("       ERP SALES ANALYSIS REPORT")
print("=" * 45)
print(f"  Period         : {date_from} to {date_to}")
print(f"  Total Orders   : {total_orders:,}")
print(f"  Total Revenue  : ${total_revenue:,.2f}")
print(f"  Avg Order Value: ${avg_order_value:,.2f}")
print("-" * 45)
print(f"  Best Month     : {best_month} (${best_month_revenue:,.2f})")
print(f"  Top Customer   : ID {top_customer_id} (${top_customer_revenue:,.2f})")
print("=" * 45)

# Save report as text file
report_path = os.path.join(base_dir, "data", "summary_report.txt")
with open(report_path, "w") as f:
    f.write("=" * 45 + "\n")
    f.write("       ERP SALES ANALYSIS REPORT\n")
    f.write("=" * 45 + "\n")
    f.write(f"  Period         : {date_from} to {date_to}\n")
    f.write(f"  Total Orders   : {total_orders:,}\n")
    f.write(f"  Total Revenue  : ${total_revenue:,.2f}\n")
    f.write(f"  Avg Order Value: ${avg_order_value:,.2f}\n")
    f.write("-" * 45 + "\n")
    f.write(f"  Best Month     : {best_month} (${best_month_revenue:,.2f})\n")
    f.write(f"  Top Customer   : ID {top_customer_id} (${top_customer_revenue:,.2f})\n")
    f.write("=" * 45 + "\n")

print("\nReport saved to data/summary_report.txt")