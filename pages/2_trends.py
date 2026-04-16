import streamlit as st
from modules.processor import process_data
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="Trends and Insights")

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