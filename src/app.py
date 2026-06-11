import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page config
st.set_page_config(page_title="ERP Sales Dashboard", layout="wide")

# Title
st.title("🏭 ERP Sales Analytics Dashboard")
st.markdown("**AdventureWorks Sales Data | 2011–2014**")

# Load data
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

orders = pd.read_csv(os.path.join(base_dir, "data", "clean_orders.csv"))
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["Month"] = orders["OrderDate"].dt.to_period("M")

monthly_revenue = orders.groupby("Month")["TotalDue"].sum().reset_index()
monthly_revenue["Month"] = monthly_revenue["Month"].astype(str)

top_customers = orders.groupby("CustomerID")["TotalDue"].sum().sort_values(ascending=False).head(10).reset_index()
top_customers["CustomerID"] = top_customers["CustomerID"].astype(str)

# --- KPI Cards ---
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Revenue", f"${orders['TotalDue'].sum():,.0f}")
col2.metric("📦 Total Orders", f"{len(orders):,}")
col3.metric("🧾 Avg Order Value", f"${orders['TotalDue'].mean():,.0f}")

st.markdown("---")

# --- Charts side by side ---
col4, col5 = st.columns(2)

with col4:
    st.subheader("📈 Monthly Revenue Trend")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(monthly_revenue["Month"], monthly_revenue["TotalDue"], marker="o", color="steelblue")
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig1)

with col5:
    st.subheader("🏆 Top 10 Customers by Revenue")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.barh(top_customers["CustomerID"], top_customers["TotalDue"], color="coral")
    ax2.set_xlabel("Total Revenue ($)")
    ax2.set_ylabel("Customer ID")
    plt.tight_layout()
    st.pyplot(fig2)

st.markdown("---")

# --- Raw Data Table ---
st.subheader("📋 Raw Orders Data")
st.dataframe(orders.head(50))