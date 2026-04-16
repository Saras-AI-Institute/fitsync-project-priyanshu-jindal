import streamlit as st
from modules.processor import process_data
import pandas as pd  # Make sure to import pandas for handling date ranges
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="FitSync")

# Page Title
st.title("FitSync - Personal Health Analysis")

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

# Calculate metrics from the filtered data
average_steps = df['Steps'].mean()
average_sleep_hours = df['Sleep_Hours'].mean()
average_recovery_score = df['Recovery_Score'].mean()

# Display metrics in a 3-column layout
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Average Steps", value=f"{average_steps:.0f}", delta=None)

with col2:
    st.metric(label="Average Sleep Hours", value=f"{average_sleep_hours:.1f}", delta=None)

with col3:
    st.metric(label="Average Recovery Score", value=f"{average_recovery_score:.1f}", delta=None)

st.write("Explore your health metrics in depth with FitSync")

# Columns for additional plots
left_col1, right_col1 = st.columns(2)

# Dual Line Chart for Recovery Score & Sleep Trend
with left_col1:
    fig = px.line(df, x='Date', y=['Recovery_Score', 'Sleep_Hours'],
                  labels={'value': 'Metrics', 'Date': 'Date'},
                  title='Recovery Score & Sleep Trend')
    st.plotly_chart(fig, use_container_width=True)

# Scatter Plot for Recovery Score vs Steps
with right_col1:
    fig = px.scatter(df, x='Steps', y='Recovery_Score', color='Sleep_Hours',
                      labels={'Steps': 'Daily Steps', 'Recovery_Score': 'Recovery Score'},
                      title='Recovery Score vs Daily Steps')
    st.plotly_chart(fig, use_container_width=True)

# Columns for additional plots
left_col2, right_col2 = st.columns(2)

# Scatter Plot for Recovery Score vs Heart Rate
with left_col2:
    fig = px.scatter(df, x='Heart_Rate_bpm', y='Recovery_Score',
                      labels={'Heart_Rate_bpm': 'Heart Rate (bpm)', 'Recovery_Score': 'Recovery Score'},
                      title='Recovery Score vs Heart Rate')
    st.plotly_chart(fig, use_container_width=True)

# Line Chart for Calories Burned Trend
with right_col2:
    fig = px.line(df, x='Date', y='Calories_Burned',
                  labels={'Calories_Burned': 'Calories Burned', 'Date': 'Date'},
                  title='Daily Calories Burned Trend')
    st.plotly_chart(fig, use_container_width=True)

# Note: This is a basic template. You can expand with actual summaries and charts using st.pyplot, st.bar_chart, etc.

# Comments to guide future enhancements
# - Ensure to keep data updated
# - Consider user interactivity features with charts
# - Optimize the performance for handling large datasets