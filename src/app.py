import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Page config
st.set_page_config(page_title="ERP Sales Dashboard", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        body { background-color: #f4f6f9; }
        .main { background-color: #f4f6f9; }
        .block-container { padding: 2rem 3rem; }
        h1 { text-align: center; color: #1a1a2e; font-size: 2.2rem; }
        h2 { text-align: center; color: #16213e; }
        .subtitle { text-align: center; color: #555; font-size: 1rem; margin-top: -10px; margin-bottom: 20px; }
        .kpi-box {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .kpi-label { font-size: 0.85rem; color: #888; text-transform: uppercase; letter-spacing: 1px; }
        .kpi-value { font-size: 1.8rem; font-weight: 700; color: #1a1a2e; margin-top: 4px; }
        .section-divider { margin: 2rem 0; border: none; border-top: 1px solid #e0e0e0; }
    </style>
""", unsafe_allow_html=True)

# Load data
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
orders = pd.read_csv(os.path.join(base_dir, "data", "clean_orders.csv"))
orders["OrderDate"] = pd.to_datetime(orders["OrderDate"])
orders["Month"] = orders["OrderDate"].dt.to_period("M")

monthly_revenue = orders.groupby("Month")["TotalDue"].sum().reset_index()
monthly_revenue["Month"] = monthly_revenue["Month"].astype(str)

top_customers = orders.groupby("CustomerID")["TotalDue"].sum().sort_values(ascending=False).head(10).reset_index()
top_customers["CustomerID"] = top_customers["CustomerID"].astype(str)

# Header
st.markdown("<h1>ERP Sales Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown('<p class="subtitle">AdventureWorks Sales Data | May 2011 - Jun 2014</p>', unsafe_allow_html=True)
st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">Total Revenue</div>
            <div class="kpi-value">${orders['TotalDue'].sum():,.0f}</div>
        </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">Total Orders</div>
            <div class="kpi-value">{len(orders):,}</div>
        </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""
        <div class="kpi-box">
            <div class="kpi-label">Avg Order Value</div>
            <div class="kpi-value">${orders['TotalDue'].mean():,.0f}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# Charts
col4, col5 = st.columns(2)

with col4:
    st.markdown("<h4 style='text-align:center;color:#1a1a2e;'>Monthly Revenue Trend</h4>", unsafe_allow_html=True)
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    fig1.patch.set_facecolor('#ffffff')
    ax1.set_facecolor('#f9f9f9')
    ax1.plot(monthly_revenue["Month"], monthly_revenue["TotalDue"],
             marker="o", color="#0f3460", linewidth=2, markersize=4)
    ax1.fill_between(monthly_revenue["Month"], monthly_revenue["TotalDue"],
                     alpha=0.1, color="#0f3460")
    ax1.set_xlabel("Month", fontsize=9, color="#555")
    ax1.set_ylabel("Revenue ($)", fontsize=9, color="#555")
    ax1.tick_params(axis='x', rotation=45, labelsize=7)
    ax1.tick_params(axis='y', labelsize=7)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig1)

with col5:
    st.markdown("<h4 style='text-align:center;color:#1a1a2e;'>Top 10 Customers by Revenue</h4>", unsafe_allow_html=True)
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    fig2.patch.set_facecolor('#ffffff')
    ax2.set_facecolor('#f9f9f9')
    bars = ax2.barh(top_customers["CustomerID"], top_customers["TotalDue"],
                    color="#e94560", edgecolor='none', height=0.6)
    ax2.set_xlabel("Total Revenue ($)", fontsize=9, color="#555")
    ax2.set_ylabel("Customer ID", fontsize=9, color="#555")
    ax2.tick_params(labelsize=7)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig2)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)

# Raw Data Table
st.markdown("<h4 style='text-align:center;color:#1a1a2e;'>Raw Orders Data</h4>", unsafe_allow_html=True)
display_cols = ["SalesOrderID", "OrderDate", "CustomerID", "SubTotal", "TaxAmt", "TotalDue"]
st.dataframe(
    orders[display_cols].head(50).reset_index(drop=True),
    use_container_width=True
)
