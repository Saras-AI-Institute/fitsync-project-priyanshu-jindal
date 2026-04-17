import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="Trends and Insights")

# Initialize session state for theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

# Extract CSS based on theme
def get_css(theme):
    if theme == 'dark':
        return """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600&family=DM+Sans&display=swap');
            body, .stApp { background-color: #0e153a !important; color: #ffffff; font-family: 'DM Sans', sans-serif; }
            h1, h2, h3, h4 { font-family: 'Syne', sans-serif; color: #00d4ff; margin-bottom: 0; }
            .headline-gradient {
                font-size: 3.7rem;
                background: linear-gradient(120deg, #00f5a0, #00d4ff);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                margin: 25px 0 20px; text-align: center;
            }
            .pill-badge {
                display: block; padding: 12px 30px; border-radius: 25px;
                background-color: #00f5a0; color: #0e153a;
                margin: 20px auto; font-size: 1.1rem; font-weight: bold; text-align: center; width: fit-content;
            }
            .metric-card {
                border-radius: 12px; padding: 25px; background-color: #1f2440;
                color: #ffffff; text-align: center;
                box-shadow: 0 6px 18px rgba(0,0,0,0.2); margin: 15px 0;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .metric-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.3); }
            .metric-card h3 { margin: 15px 0 10px; color: #29abe2; }
            .metric-card .value { font-size: 2.7rem; font-weight: bold; color: #ffffff; }
            .metric-card .label { text-transform: uppercase; font-size: 0.9rem; color: #cccccc; }
            .pro-tip {
                background-color: #1b1b33; padding: 15px; border-radius: 10px;
                display: flex; align-items: center;
                box-shadow: 0 3px 12px rgba(0,0,0,0.25); margin-top: 45px; color: #ffffff;
            }
            .pro-tip-icon { margin-right: 12px; font-size: 1.8rem; color: #00f5a0; }
            .sidebar-arrow { animation: bounce 2s infinite; margin: 25px 0; color: #00f5a0; font-size: 2rem; text-align: center; }
            .hr-divider { border: none; height: 1px; background: linear-gradient(90deg, #00f5a0, #00d4ff); margin: 20px 0; }
            footer { display: none; } header { display: none; }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-12px); }
                60% { transform: translateY(-6px); }
            }
        </style>
        """
    else:
        return """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Syne:wght@600&family=DM+Sans&display=swap');
            body, .stApp { background-color: #f4f6fb !important; color: #1a1a2e; font-family: 'DM Sans', sans-serif; }
            h1, h2, h3, h4 { font-family: 'Syne', sans-serif; color: #0077b6; margin-bottom: 0; }
            .headline-gradient {
                font-size: 3.7rem;
                background: linear-gradient(120deg, #00a86b, #0077b6);
                -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                margin: 25px 0 20px; text-align: center;
            }
            .pill-badge {
                display: block; padding: 12px 30px; border-radius: 25px;
                background-color: #0077b6; color: #ffffff;
                margin: 20px auto; font-size: 1.1rem; font-weight: bold; text-align: center; width: fit-content;
            }
            .metric-card {
                border-radius: 12px; padding: 25px; background-color: #ffffff;
                color: #1a1a2e; text-align: center;
                box-shadow: 0 6px 18px rgba(0,0,0,0.08); margin: 15px 0;
                transition: transform 0.2s, box-shadow 0.2s;
            }
            .metric-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.12); }
            .metric-card h3 { margin: 15px 0 10px; color: #0077b6; }
            .metric-card .value { font-size: 2.7rem; font-weight: bold; color: #1a1a2e; }
            .metric-card .label { text-transform: uppercase; font-size: 0.9rem; color: #555555; }
            .pro-tip {
                background-color: #e8f4fd; padding: 15px; border-radius: 10px;
                display: flex; align-items: center;
                box-shadow: 0 3px 12px rgba(0,0,0,0.06); margin-top: 45px; color: #1a1a2e;
            }
            .pro-tip-icon { margin-right: 12px; font-size: 1.8rem; color: #0077b6; }
            .sidebar-arrow { animation: bounce 2s infinite; margin: 25px 0; color: #0077b6; font-size: 2rem; text-align: center; }
            .hr-divider { border: none; height: 1px; background: linear-gradient(90deg, #00a86b, #0077b6); margin: 20px 0; }
            footer { display: none; } header { display: none; }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
                40% { transform: translateY(-12px); }
                60% { transform: translateY(-6px); }
            }
        </style>
        """

# Inject the appropriate CSS based on the theme
st.markdown(get_css(st.session_state.theme), unsafe_allow_html=True)

# Toggle Theme Button
def toggle_theme():
    st.session_state.theme = 'light' if st.session_state.theme == 'dark' else 'dark'

# Add Button at the Top to Switch Themes
_, theme_button_col = st.columns([9, 1])
with theme_button_col:
    button_label = "☀️ Light Mode" if st.session_state.theme == 'dark' else "🌙 Dark Mode"
    st.button(button_label, on_click=toggle_theme)

# Page Title
st.title("Trends and Insights")

# Sidebar filter for time range
st.sidebar.header("Filter")
time_range = st.sidebar.selectbox(
    "Select Time Range",
    options=["Last 7 Days", "Last 30 Days", "All time"],
    index=2
)

# Load the data
df = process_data()

# Filter the dataframe based on the selected time range
if time_range == "Last 7 Days":
    df = df[df['Date'] >= df['Date'].max() - pd.Timedelta(days=7)]
elif time_range == "Last 30 Days":
    df = df[df['Date'] >= df['Date'].max() - pd.Timedelta(days=30)]
# "All time" uses the full dataframe by default

# Calculate summary statistics
summary_stats = df[['Recovery_Score', 'Sleep_Hours', 'Steps', 'Calories_Burned']].agg(['mean', 'min', 'max'])
st.write("### Summary Statistics")
st.dataframe(summary_stats)

# Monthly Average Recovery Score
monthly_avg_recovery = df.resample('M', on='Date').mean().reset_index()
avg_recovery_fig = px.line(monthly_avg_recovery, x='Date', y='Recovery_Score',
                          title='Monthly Average Recovery Score')

st.plotly_chart(avg_recovery_fig, use_container_width=True)

# Histogram distributions
st.write("### Histogram Distributions")
fig_steps = px.histogram(df, x='Steps', title='Steps Distribution')
fig_calories = px.histogram(df, x='Calories_Burned', title='Calories Burned Distribution')
fig_recovery = px.histogram(df, x='Recovery_Score', title='Recovery Score Distribution')
fig_sleep = px.histogram(df, x='Sleep_Hours', title='Sleep Hours Distribution')

st.plotly_chart(fig_steps, use_container_width=True)
st.plotly_chart(fig_calories, use_container_width=True)
st.plotly_chart(fig_recovery, use_container_width=True)
st.plotly_chart(fig_sleep, use_container_width=True)