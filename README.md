<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:050505,45:15151f,75:e10600,100:ff8700&height=190&section=header&text=F1%20RACING%20ANALYTICS&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=34" width="100%"/>

<br>

<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=700&size=20&duration=2200&pause=800&color=FF8700&center=true&vCenter=true&width=720&lines=LIGHTS+OUT.+DATA+IN.;Explore+the+numbers+behind+the+race.;A+small+F1+hobby+project+by+Sujal+Makwana." />

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![FastF1](https://img.shields.io/badge/FastF1-E10600?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge\&logo=pandas\&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-111111?style=for-the-badge\&logo=plotly\&logoColor=white)

<br><br>

<img src="assets/f1-car.gif" width="720" alt="F1 car racing animation"/>

</div>

---

# 🏁 About The Project

**F1 Racing Analytics** is a small hobby project I built because I wanted to play around with Formula 1 data and see what could be extracted from it.

Instead of treating race results as a simple table, I wanted to turn them into an interactive experience where you can explore:

**🏎️ race results · ⚔️ driver battles · 🏆 team performance · 📊 visual analysis**

The project uses **FastF1** to fetch F1 timing and telemetry data, then processes and visualizes it through Python, Pandas, Plotly and Streamlit.

> Built as a hobby project. Built because F1 is fun. 🏎️💨

---

# 🚦 Race Mode

<table>
<tr>

<td width="50%" align="center">

### 📡 DATA FEED

Dynamic F1 session data through **FastF1**

</td>

<td width="50%" align="center">

### ⚔️ DRIVER BATTLE

Select two drivers and compare them directly

</td>

</tr>

<tr>

<td width="50%" align="center">

### 🏆 TEAM PACE

Explore race results and team performance

</td>

<td width="50%" align="center">

### 📊 TELEMETRY

Turn timing and race data into interactive charts

</td>

</tr>
</table>

---

# 🏎️ Driver Battle

The fun part.

Choose two drivers and put them head-to-head.

```text
           DRIVER A
               │
               ▼
        ┌─────────────┐
        │   FASTF1    │
        └──────┬──────┘
               │
               ▼
            PANDAS
               │
        ┌──────┴──────┐
        ▼             ▼
    DRIVER A       DRIVER B
        │             │
        └──────┬──────┘
               ▼
        ⚔️ HEAD-TO-HEAD
               │
               ▼
      📊 INTERACTIVE CHART
```

---

# 📊 What You Can Explore

```text
🏁 Race Results
⚔️ Driver vs Driver
🏆 Team Performance
📈 Interactive Charts
📡 Timing & Telemetry Data
🔎 Dynamic Filtering
```

---

# 🖥️ The Race Hub

<!-- Add your actual dashboard screenshot here -->

<div align="center">

### FROM THE GRID TO THE CHECKERED FLAG

**Race data → analysis → visualization**

</div>

---

# 🏁 Data Pipeline

```text
       🏎️ F1 SESSION
            │
            ▼
       ┌──────────┐
       │  FastF1  │
       └────┬─────┘
            │
            ▼
       ┌──────────┐
       │  Pandas  │
       └────┬─────┘
            │
     ┌──────┴──────┐
     ▼             ▼
🏆 Team Data    ⚔️ Driver Data
     │             │
     └──────┬──────┘
            ▼
       ┌──────────┐
       │  Plotly  │
       └────┬─────┘
            │
            ▼
       🏎️ Streamlit
```

---

# ⚡ Performance

Working with F1 session data can mean fetching and processing the same information repeatedly.

To keep the app responsive, the project uses **Streamlit caching** and optimized data requests.

```python
@st.cache_data
```

So the same session doesn't need to be rebuilt every single time.

---

# 🛠️ Tech Stack

| Category           | Technology      |
| ------------------ | --------------- |
| 🐍 Language        | Python 3        |
| 🏎️ F1 Data        | FastF1          |
| 📊 Data Processing | Pandas          |
| 📈 Visualization   | Plotly          |
| 🖥️ Application    | Streamlit       |
| ⚡ Optimization     | Streamlit Cache |

---

# 🚀 Run It Locally

### 1. Clone

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

### 4. Start the race

```bash
streamlit run app.py
```

---

# 🔮 Next Lap

This project started as a hobby experiment, but there are plenty of ways it could grow.

```text
Current
   │
   ├── Race Results
   ├── Driver Comparisons
   └── Team Analysis
   │
   ▼
Next Lap
   │
   ├── Lap-by-lap analysis
   ├── Deeper telemetry views
   ├── Multi-driver battles
   ├── Constructor analysis
   └── Race-weekend mode
```

---

# 🏎️ Why I Built It

No big corporate story here.

I like F1.

I wanted to work with real motorsport data, play with visualizations, and see if I could turn race numbers into something interactive.

So I built it.

**That's it. That's the project.** 😂

---

<div align="center">

## 🔴 LIGHTS OUT

### 🟢 AND AWAY WE GO.

<br>

**Built by Sujal Makwana**

<br>

<img src="https://img.shields.io/badge/STATUS-HOBBY%20PROJECT-E10600?style=for-the-badge"/>
<img src="https://img.shields.io/badge/BUILT%20FOR-F1%20FANS-FF8700?style=for-the-badge"/>

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff8700,45:e10600,100:050505&height=110&section=footer" width="100%"/>
