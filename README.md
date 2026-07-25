📊 ESG Dashboard

A real-time ESG (Environmental, Social, Governance) scoring dashboard built with Streamlit, pulling company sustainability data from the S&P Global Market Intelligence ESG API.

Problem Statement

ESG performance is increasingly used by investors, regulators, and stakeholders to evaluate companies beyond pure financials. Raw ESG data from providers is often locked in APIs and hard to interpret at a glance. This dashboard turns that raw data into a live, visual, executive-style view of a company's ESG standing — score breakdowns, risk level, and category-wise analysis — updated automatically.

Features
🔄 Auto-refreshing dashboard — pulls fresh data every 60 seconds without manual reload
📈 KPI cards for overall ESG score plus Environmental, Social, and Governance sub-scores
📊 Visual breakdown via bar chart and pie chart (Plotly)
🗂️ Category tabs — dedicated views for Environmental, Social, and Governance details, including a carbon emissions indicator
🚦 Automated risk classification — flags overall ESG risk as Strong / Moderate / High based on score thresholds
🛡️ Graceful fallback — if the API is unreachable or unauthenticated, the dashboard displays reasonable demo values instead of crashing, so the UI is always demonstrable
Tech Stack
Frontend/App: Streamlit, streamlit-option-menu, streamlit-autorefresh
Data & Visualization: Pandas, Plotly Express
Data Source: S&P Global Market Intelligence ESG API
Language: Python 3
Installation
bash
# Clone the repository
git clone https://github.com/Atharvmukadam/esg-dashboard-infosys.git
cd esg-dashboard-infosys

# Install dependencies
pip install -r requirements.txt
API Key Setup

This project pulls live data from the S&P Global Market Intelligence ESG API, which requires a registered API key.

Obtain an API key from S&P Global Market Intelligence
Replace "YOUR_SMP_API_KEY" in api.py (and app.py) with your key — ideally via an environment variable rather than hardcoding it:
python
import os
API_KEY = os.getenv("SMP_API_KEY")

Note: Without a valid key, the dashboard still runs — it automatically falls back to demo ESG values so the UI remains fully explorable.

Usage
bash
streamlit run app.py

The dashboard opens in your browser at http://localhost:8501. Use the sidebar to navigate between Overview, Environmental, Social, and Governance views. The default tracked company is Infosys (INFY) — this can be changed by editing the company parameter passed to get_esg_data().

Folder Structure
esg-dashboard-infosys/
├── app.py              # Main Streamlit application (UI + dashboard logic)
├── api.py              # ESG data-fetching logic (S&P Global API wrapper)
├── utils.py            # Data processing / transformation helpers
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime version (for deployment)
└── .gitignore
Future Improvements
 Remove duplicated get_esg_data() logic from app.py and import it from api.py instead, to keep data-fetching logic in one place
 Move the API key to an environment variable / .env file instead of a placeholder string in source
 Add support for tracking and comparing multiple companies side-by-side
 Add historical ESG score trend charts (line chart over time) instead of only current snapshot
 Deploy publicly (e.g. Streamlit Community Cloud) and link the live demo here
Author

Atharv Mukadam — LinkedIn
