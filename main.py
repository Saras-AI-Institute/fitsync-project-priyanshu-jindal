import streamlit as st
from modules.processor import process_data
import pandas as pd  # Make sure to import pandas for handling date ranges

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

# Note: This is a basic template. You can expand with actual summaries and charts using st.pyplot, st.bar_chart, etc.