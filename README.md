# f1_deshboard
 # 🏎️ F1 Race Results Dashboard

An interactive, real-time data visualization dashboard built with Python and Streamlit. This tool fetches official Formula 1 timing and telemetry data to visualize race outcomes, team dominance, and head-to-head driver comparisons.

## 🚀 Features
* **Live API Integration:** Pulls dynamic race data using the `fastf1` library.
* **Custom Data Visualization:** Utilizes `plotly.express` for interactive charts with official F1 team color mapping.
* **Dynamic Filtering:** Head-to-head multiselect tools to compare specific drivers instantly.
* **Optimized Performance:** Implements Streamlit caching (`@st.cache_data`) and optimized payload requests for blazing-fast load times.

## 🛠️ Tech Stack
* Python 3
* Streamlit
* Pandas
* Plotly
* FastF1

## 💻 How to Run Locally
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run the app: `streamlit run app.py`
