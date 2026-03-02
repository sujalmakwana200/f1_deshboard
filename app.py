import streamlit as st
import plotly.express as px
import fastf1
import pandas as pd
import os

# Set up the cache directory for FastF1
cache_dir = './data_cache'
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
fastf1.Cache.enable_cache(cache_dir)    

# Page configuration
st.set_page_config(page_title="F1 Driver Standings", layout="wide")
st.title("🏎️ F1 Race Results Dashboard")

# Sidebar inputs
st.sidebar.header("Select Race Details")
year = st.sidebar.number_input("Year", min_value=2018, max_value=2025, value=2024)
gp = st.sidebar.text_input("Grand Prix Name (e.g., Monaco)", value="Monaco")
session_type = st.sidebar.selectbox("Session", ["Race", "Qualifying"])

# Fetch data function (Optimized for speed)
@st.cache_data
def get_race_results(year, gp, session_type):
    session_code = 'R' if session_type == "Race" else 'Q'
    session = fastf1.get_session(year, gp, session_code)
    session.load(telemetry=False, weather=False, messages=False)
    return session.results

# We removed the button! Now it runs dynamically.
with st.spinner(f"Fetching data for {year} {gp}..."):
    try:
        results = get_race_results(year, gp, session_type)    
        
        # Filter the dataframe for display
        display_df = results[['ClassifiedPosition', 'FullName','TeamName','Abbreviation','Points']]
            
        st.header(f"🏁 Results for {year} {gp}")
            
        # FEATURE 1: KPI Metric Cards for the Podium
        st.subheader("Podium Finishers")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(label="🥇 1st Place", value=display_df.iloc[0]['FullName'], delta=f"{display_df.iloc[0]['Points']} pts")
        with col2:
            st.metric(label="🥈 2nd Place", value=display_df.iloc[1]['FullName'], delta=f"{display_df.iloc[1]['Points']} pts")
        with col3:
            st.metric(label="🥉 3rd Place", value=display_df.iloc[2]['FullName'], delta=f"{display_df.iloc[2]['Points']} pts")

        st.divider()

        # Official F1 Team Colors
        team_colors = {
            'Ferrari': '#E80020',
            'McLaren': '#FF8700',
            'Mercedes': '#27F4D2',
            'Red Bull Racing': '#3671C6',
            'RB': '#6692FF',
            'Williams': '#64C4FF',
            'Alpine': '#FF87BC',
            'Aston Martin': '#229971',
            'Kick Sauber': '#52E252',
            'Haas F1 Team': '#B6BABD'
        }

        # FEATURE 2: Bar Chart
        st.subheader("Driver Points Distribution")
        points_df = display_df[display_df['Points'] > 0]
        fig_bar = px.bar(
            points_df, x='Abbreviation', y='Points', color='TeamName',
            labels={'Abbreviation': 'Driver', 'Points': 'Points Scored'},
            text_auto=True, color_discrete_map=team_colors
        )
        st.plotly_chart(fig_bar, theme=None, use_container_width=True)

        # FEATURE 3: Team Dominance Donut Chart
        st.subheader("Team Dominance (Total Points)")
        team_points_df = points_df.groupby('TeamName', as_index=False)['Points'].sum()
        fig_donut = px.pie(
            team_points_df, values='Points', names='TeamName', 
            hole=0.4, color='TeamName', color_discrete_map=team_colors
        )
        fig_donut.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_donut, theme=None, use_container_width=True)

        # FEATURE 4: Driver Comparison Tool
        st.divider()
        st.subheader("🏎️ Head-to-Head Driver Comparison")
        
        driver_list = display_df['FullName'].tolist()
        selected_drivers = st.multiselect(
            "Select drivers to compare:",
            options=driver_list,
            default=driver_list[:2] 
        )
        
        if selected_drivers:
            comparison_df = display_df[display_df['FullName'].isin(selected_drivers)]
            st.dataframe(comparison_df, use_container_width=True)
        else:
            st.info("Please select at least one driver to see the comparison.")

        # FEATURE 5: UI Expander for Raw Data
        with st.expander("📊 View Raw Race Data"):
            st.dataframe(display_df, use_container_width=True)
            
    except Exception as e:
        st.error("Could not load data for this race. Please check your inputs!")
