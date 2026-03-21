import streamlit as st
from streamlit_echarts import st_echarts
import fastf1
import pandas as pd
import os

# 1. Page Configuration
st.set_page_config(page_title="F1 Intelligence Engine", layout="wide")

# 2. Bespoke UI (True Black + Hiding Branding)
hide_streamlit_style = """
            <style>
            [data-testid="stAppViewContainer"] { background-color: #000000; }
            [data-testid="stHeader"] { background-color: rgba(0,0,0,0); }
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div[data-testid="metric-container"] {
                background-color: #0A0A0A;
                border-radius: 8px;
                padding: 15px;
                border: 1px solid #222222;
                box-shadow: 0 4px 6px rgba(0,0,0,0.5);
            }
            p, h1, h2, h3, h4, h5, h6, label { color: #FFFFFF !important; }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Set up cache
cache_dir = './data_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
fastf1.Cache.enable_cache(cache_dir)    

st.title("F1 Telemetry & Results Architecture")
st.markdown("Enterprise-grade race intelligence featuring dynamic state transitions.")

# 3. Top-Bar Control Panel
st.markdown("### Telemetry Controls")
with st.form("telemetry_form"):
    ctrl1, ctrl2, ctrl3 = st.columns(3)

    with ctrl1:
        year = st.selectbox("Championship Year", list(range(2025, 2017, -1)))
    with ctrl2:
        gp_calendar = [
            "Bahrain", "Saudi Arabia", "Australia", "Japan", "China", "Miami", 
            "Emilia Romagna", "Monaco", "Canada", "Spain", "Austria", "Great Britain", 
            "Hungary", "Belgium", "Netherlands", "Italy", "Azerbaijan", "Singapore", 
            "United States", "Mexico", "Sao Paulo", "Las Vegas", "Qatar", "Abu Dhabi"
        ]
        gp = st.selectbox("Grand Prix", gp_calendar, index=7)
    with ctrl3:
        session_type = st.selectbox("Session Target", ["Race", "Qualifying"])
    
    submit_sync = st.form_submit_button("Initiate Telemetry Sync")

st.divider()

# 4. Enterprise Session State Management
if submit_sync:
    st.session_state['sync_active'] = True
    st.session_state['year'] = year
    st.session_state['gp'] = gp
    st.session_state['session_type'] = session_type

@st.cache_data(ttl=3600) 
def get_race_results(year, gp, session_type):
    session_code = 'R' if session_type == "Race" else 'Q'
    session = fastf1.get_session(year, gp, session_code)
    session.load(telemetry=False, weather=False, messages=False)
    return session.results

# 5. Core Engine Execution
if st.session_state.get('sync_active', False):
    active_year = st.session_state['year']
    active_gp = st.session_state['gp']
    active_session = st.session_state['session_type']

    with st.spinner(f"Establishing secure connection to {active_year} {active_gp} database..."):
        try:
            results = get_race_results(active_year, active_gp, active_session)    
            
            display_df = results[['ClassifiedPosition', 'GridPosition', 'FullName', 'TeamName', 'Abbreviation', 'Points']]
                
            # FEATURE 1: Premium KPI Metric Cards
            st.subheader("Podium Architecture")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric(label="P1 Finisher", value=display_df.iloc[0]['FullName'], delta=f"{display_df.iloc[0]['Points']} Points Scored")
            with col2:
                st.metric(label="P2 Finisher", value=display_df.iloc[1]['FullName'], delta=f"{display_df.iloc[1]['Points']} Points Scored", delta_color="off")
            with col3:
                st.metric(label="P3 Finisher", value=display_df.iloc[2]['FullName'], delta=f"{display_df.iloc[2]['Points']} Points Scored", delta_color="off")

            st.divider()

            team_colors = {
                'Ferrari': '#E80020', 'McLaren': '#FF8700', 'Mercedes': '#27F4D2',
                'Red Bull Racing': '#3671C6', 'RB': '#6692FF', 'Williams': '#64C4FF',
                'Alpine': '#FF87BC', 'Aston Martin': '#229971', 'Kick Sauber': '#52E252',
                'Haas F1 Team': '#B6BABD'
            }

            # FEATURE 2 & 3: Dashboard Density (Transition Animations)
            st.subheader("Performance Distribution Matrix")
            points_df = display_df[display_df['Points'] > 0]

            if not points_df.empty:
                chart_col1, chart_col2 = st.columns((2, 1))

                with chart_col1:
                    bar_data = [{"value": row['Points'], "itemStyle": {"color": team_colors.get(row['TeamName'], '#333333')}} for index, row in points_df.iterrows()]
                    bar_options = {
                        "animation": True,
                        "animationDuration": 2000,              
                        "animationDurationUpdate": 2000,        # This makes the bars morph when changing races
                        "animationEasing": "cubicOut",
                        "animationEasingUpdate": "cubicOut",
                        "title": {"text": "Driver Point Allocation", "textStyle": {"color": "#FFFFFF"}},
                        "tooltip": {"trigger": "axis"},
                        "xAxis": {"type": "category", "data": points_df['Abbreviation'].tolist(), "axisLabel": {"color": "#FFFFFF"}},
                        "yAxis": {"type": "value", "axisLabel": {"color": "#FFFFFF"}, "splitLine": {"lineStyle": {"color": "#222222"}}},
                        "series": [{"data": bar_data, "type": "bar", "label": {"show": True, "position": "top", "color": "#FFFFFF"}}]
                    }
                    # Removed the unique key so Streamlit updates the existing chart instead of destroying it
                    st_echarts(options=bar_options, height="400px")

                with chart_col2:
                    team_points_df = points_df.groupby('TeamName', as_index=False)['Points'].sum()
                    donut_data = [{"value": row['Points'], "name": row['TeamName'], "itemStyle": {"color": team_colors.get(row['TeamName'], '#333333')}} for index, row in team_points_df.iterrows()]
                    donut_options = {
                        "animation": True,
                        "animationDuration": 2000,
                        "animationDurationUpdate": 2000,        # This makes the donut slices shift when changing races
                        "animationEasing": "cubicOut",
                        "animationEasingUpdate": "cubicOut",
                        "title": {"text": "Constructor Dominance", "textStyle": {"color": "#FFFFFF"}, "left": "center"},
                        "tooltip": {"trigger": "item"},
                        "series": [{"type": "pie", "radius": ["40%", "70%"], "data": donut_data, "label": {"color": "#FFFFFF"}}]
                    }
                    # Removed the unique key
                    st_echarts(options=donut_options, height="400px")
            else:
                st.info("System Notice: No championship points were awarded in this specific session. Distribution matrix is offline.")

            st.divider()

            # FEATURE 4: Head-to-Head Visual Comparison
            st.subheader("Head-to-Head Telemetry Comparison")
            
            driver_list = display_df['FullName'].tolist()
            selected_drivers = st.multiselect(
                "Select exactly two drivers to initiate comparison matrix:",
                options=driver_list,
                default=driver_list[:2],
                max_selections=2
            )
            
            if len(selected_drivers) == 2:
                comp_df = display_df[display_df['FullName'].isin(selected_drivers)]
                driver1, driver2 = comp_df.iloc[0], comp_df.iloc[1]
                
                d1_col, d2_col = st.columns(2)
                
                with d1_col:
                    st.markdown(f"<h3 style='text-align: center; color: #FFFFFF;'>{driver1['FullName']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; color: #888888;'>{driver1['TeamName']}</p>", unsafe_allow_html=True)
                    st.metric("Final Race Position", f"P{driver1['ClassifiedPosition']}")
                    st.metric("Starting Grid Position", f"P{driver1['GridPosition']}")
                    st.metric("Championship Points", driver1['Points'])
                    
                with d2_col:
                    st.markdown(f"<h3 style='text-align: center; color: #FFFFFF;'>{driver2['FullName']}</h3>", unsafe_allow_html=True)
                    st.markdown(f"<p style='text-align: center; color: #888888;'>{driver2['TeamName']}</p>", unsafe_allow_html=True)
                    st.metric("Final Race Position", f"P{driver2['ClassifiedPosition']}")
                    st.metric("Starting Grid Position", f"P{driver2['GridPosition']}")
                    st.metric("Championship Points", driver2['Points'])
                    
            elif len(selected_drivers) == 1:
                st.info("System Notice: Select one additional driver to render the comparison matrix.")
            else:
                st.info("System Notice: Awaiting driver selection for analysis.")

            # FEATURE 5: Clean Data Export
            st.markdown("<br>", unsafe_allow_html=True)
            csv = display_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export Cleaned Telemetry Data (CSV)",
                data=csv,
                file_name=f'F1_{active_year}_{active_gp}_{active_session}_Cleaned.csv',
                mime='text/csv',
            )
                
        except Exception as e:
            st.warning(f"System Notice: Unable to locate data for the {active_year} {active_gp} Grand Prix. The event may not have occurred yet, or the database is updating.")
else:
    st.info("System Ready. Configure telemetry parameters above and initiate sync.")
           
               
