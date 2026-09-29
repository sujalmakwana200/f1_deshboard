# 🏎️ F1 Racing Analytics

> **Turn race data into the story behind the lap.**

<div align="center">

![Python](https://img.shields.io/badge/Python-3-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Analytics-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![FastF1](https://img.shields.io/badge/FastF1-Race%20Data-15151E?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Engine-150458?style=for-the-badge\&logo=pandas\&logoColor=white)

</div>

---

## 🏁 The Idea

Formula 1 is more than the final classification.

Behind every result are **drivers, teams, pace, timing data and head-to-head battles**.

This project turns F1 race data into an interactive analysis experience built with **Python, FastF1, Pandas, Plotly and Streamlit**.

Instead of looking at a static race result, you can explore the data and compare the drivers and teams that shaped the session.

---

## 🚦 Race Control

### 📡 Race Data

Fetches dynamic F1 timing and telemetry data through the `FastF1` library.

### 📊 Race Visualization

Interactive Plotly charts make race results and performance patterns easier to explore.

### ⚔️ Driver vs Driver

Select drivers and instantly build head-to-head comparisons.

### 🏆 Team Performance

Explore race outcomes and identify patterns in team performance.

### ⚡ Fast Data Loading

Streamlit caching and optimized data requests reduce unnecessary reloads and improve responsiveness.

---

## 🏎️ Driver Battle Mode

One of the main parts of the project is the **head-to-head comparison workflow**.

```text
Select Driver A
       ↓
Select Driver B
       ↓
Fetch session data
       ↓
Process with Pandas
       ↓
Generate comparison
       ↓
Explore interactive charts
```

The goal is to make the numbers feel less like a spreadsheet and more like a **race battle**.

---

## 📊 What You Can Explore

```text
┌──────────────────────────────────┐
│          RACE ANALYSIS           │
├──────────────────────────────────┤
│ 🏁 Race Results                  │
│ 👤 Driver Comparisons            │
│ ⚔️ Head-to-Head Battles          │
│ 🏆 Team Performance              │
│ 📈 Interactive Visualizations    │
│ 📡 Timing & Telemetry Data       │
└──────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer           | Technology        |
| --------------- | ----------------- |
| Language        | Python 3          |
| F1 Data         | FastF1            |
| Data Processing | Pandas            |
| Visualization   | Plotly            |
| Application     | Streamlit         |
| Performance     | Streamlit caching |

---

## 🔄 Data Flow

```text
             🏎️ F1 Session Data
                     │
                     ▼
               ┌───────────┐
               │  FastF1   │
               └─────┬─────┘
                     │
                     ▼
               ┌───────────┐
               │  Pandas   │
               └─────┬─────┘
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Race Analysis          Driver Comparison
          │                     │
          └──────────┬──────────┘
                     ▼
               ┌───────────┐
               │  Plotly   │
               └─────┬─────┘
                     │
                     ▼
               🏎️ Streamlit
                 Race Hub
```

---

## 🖥️ Race Hub

<!-- Add dashboard screenshot or GIF here -->

<div align="center">

**Race results • Driver battles • Team performance • Interactive charts**

</div>

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/sujalmakwana200/f1_deshboard.git
cd f1_deshboard
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Race Hub

```bash
streamlit run app.py
```

---

## ⚡ Performance

The application uses **Streamlit caching** and optimized data requests to avoid repeatedly fetching the same session data.

```python
@st.cache_data
```

This helps keep the analysis experience responsive while working with F1 session data.

---

## 🔮 What's Next?

Possible future improvements:

* 🏁 Lap-by-lap analysis
* 📈 More detailed driver performance metrics
* ⚔️ Expanded multi-driver comparisons
* 🏆 Deeper constructor analysis
* 📡 Additional telemetry visualizations
* 🎯 Race-weekend focused views

---

## 💭 Why I Built It

I wanted to explore F1 data in a way that feels closer to **watching the race unfold** rather than reading a table of results.

This project also gave me practical experience with:

`Python` · `Pandas` · `Data Visualization` · `APIs/Data Libraries` · `Streamlit`

---

<div align="center">

## 🏁 Lights Out. Data In.

**Built by Sujal Makwana**

</div>
