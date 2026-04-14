import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from streamlit_autorefresh import st_autorefresh
from datetime import datetime
import requests

# =========================
# 🔄 AUTO REFRESH (IMPORTANT)
# =========================
st_autorefresh(interval=60000, key="refresh")  # refresh every 60 sec

# =========================
# ⚙️ CONFIG
# =========================
st.set_page_config(page_title="ESG Dashboard", layout="wide")

API_KEY = "YOUR_SMP_API_KEY"
BASE_URL = "https://api.marketintelligence.spglobal.com"

# =========================
# 📡 API FUNCTION
# =========================
def get_esg_data(company="INFY"):
    endpoint = f"/esg/v1/companies/{company}"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(BASE_URL + endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

    except Exception as e:
        return {"error": str(e)}

# =========================
# 🧹 DATA PROCESSING
# =========================
def process_esg(data):
    try:
        return {
            "ESG": data.get("esgScore", 70),
            "Environmental": data.get("environmentScore", 72),
            "Social": data.get("socialScore", 68),
            "Governance": data.get("governanceScore", 74),
            "Carbon": data.get("carbonEmission", 60)
        }
    except:
        return {
            "ESG": 70,
            "Environmental": 72,
            "Social": 68,
            "Governance": 74,
            "Carbon": 60
        }

# =========================
# 🎨 SIDEBAR
# =========================
with st.sidebar:
    selected = option_menu(
        "🌍 ESG Dashboard",
        ["Overview", "Environmental", "Social", "Governance"],
        icons=["bar-chart", "leaf", "people", "building"]
    )

# =========================
# 🏢 TITLE
# =========================
st.title("📊 Infosys ESG Dashboard")
st.caption("🔄 Auto-refresh every 60 seconds")
st.caption(f"🕒 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# =========================
# 📡 FETCH DATA
# =========================
with st.spinner("Fetching ESG data..."):
    raw_data = get_esg_data("INFY")

# =========================
# ❗ ERROR HANDLING
# =========================
if "error" in raw_data:
    st.warning("⚠️ API not responding. Showing fallback data.")
    
data = process_esg(raw_data)

# =========================
# 📊 KPI CARDS
# =========================
col1, col2, col3, col4 = st.columns(4)

col1.metric("ESG Score", data["ESG"])
col2.metric("Environmental", data["Environmental"])
col3.metric("Social", data["Social"])
col4.metric("Governance", data["Governance"])

# =========================
# 📊 CHARTS
# =========================
df = pd.DataFrame({
    "Category": ["ESG", "Environmental", "Social", "Governance"],
    "Score": [
        data["ESG"],
        data["Environmental"],
        data["Social"],
        data["Governance"]
    ]
})

colA, colB = st.columns(2)

with colA:
    fig = px.bar(df, x="Category", y="Score", title="📊 ESG Breakdown", color="Category")
    st.plotly_chart(fig, use_container_width=True)

with colB:
    fig2 = px.pie(df, names="Category", values="Score", title="📈 ESG Distribution")
    st.plotly_chart(fig2, use_container_width=True)

# =========================
# 📂 TABS
# =========================
tab1, tab2, tab3 = st.tabs(["🌱 Environmental", "👥 Social", "🏛️ Governance"])

with tab1:
    st.subheader("Environmental Analysis")
    st.progress(data["Environmental"] / 100)
    st.write("Carbon Emissions Score:", data["Carbon"])

with tab2:
    st.subheader("Social Analysis")
    st.progress(data["Social"] / 100)

with tab3:
    st.subheader("Governance Analysis")
    st.progress(data["Governance"] / 100)

# =========================
# ⚠️ ESG RISK INDICATOR
# =========================
st.subheader("🚨 ESG Risk Status")

if data["ESG"] < 50:
    st.error("🔴 High ESG Risk")
elif data["ESG"] < 70:
    st.warning("🟡 Moderate ESG Risk")
else:
    st.success("🟢 Strong ESG Performance")