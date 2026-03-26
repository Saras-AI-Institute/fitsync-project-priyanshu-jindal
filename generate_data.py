import pandas as pd
import numpy as np
from datetime import timedelta, datetime

# Parameters
days = 365
start_date = datetime.strptime('2025-01-01', '%Y-%m-%d')
nan_percentage = 0.05

# Generate dates
dates = [start_date + timedelta(days=i) for i in range(days)]

# Functions to generate realistic data
def generate_steps():
    return int(np.random.normal(8500, 3000, 1).clip(3000, 18000))

def generate_sleep_hours():
    return (np.random.normal(7.2, 1.0, 1).clip(4.5, 9.5), 1)

def generate_heart_rate():
    return int(np.random.normal(68, 10, 1).clip(48, 110))

def generate_calories_burned():
    return np.random.randint(1800, 4200)

def generate_active_minutes():
    return np.random.randint(20, 180)

# Generate data
data = {
    'Date': dates,
    'Steps': [generate_steps() for _ in range(days)],
    'Sleep_Hours': [generate_sleep_hours() for _ in range(days)],
    'Heart_Rate_bpm': [generate_heart_rate() for _ in range(days)],
    'Calories_Burned': [generate_calories_burned() for _ in range(days)],
    'Active_Minutes': [generate_active_minutes() for _ in range(days)],
}

# Create DataFrame
df = pd.DataFrame(data)

# Introduce missing values
def introduce_nans(column):
    nan_indices = np.random.choice(df.index, size=int(nan_percentage * len(df)), replace=False)
    df.loc[nan_indices, column] = np.nan

for column in df.columns[1:]:  # Skip 'Date' column
    introduce_nans(column)

# Save to CSV
output_path = 'data/health_data.csv'
df.to_csv(output_path, index=False)

print(f"Health data generated and saved to {output_path}")
