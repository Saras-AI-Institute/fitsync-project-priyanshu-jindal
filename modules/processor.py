import pandas as pd

def load_data():
    df = pd.read_csv('data/health_data.csv')

    import re
    import numpy as np

    def extract_number(x):
        if isinstance(x, str):
            match = re.search(r"\d+\.?\d*", x)
            return float(match.group()) if match else np.nan
        return x

    df['Sleep_Hours'] = df['Sleep_Hours'].apply(extract_number)

    # FORCE numeric
    df['Sleep_Hours'] = pd.to_numeric(df['Sleep_Hours'], errors='coerce')

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    df['Steps'].fillna(df['Steps'].median(), inplace=True)
    df['Sleep_Hours'].fillna(7.0, inplace=True)
    df['Heart_Rate_bpm'].fillna(68, inplace=True)

    df.fillna(df.select_dtypes(include='number').median(), inplace=True)

    return df

def calculate_recovery_score(df):
    """
    Adds a 'Recovery_Score' column to the DataFrame, ranging from 0 to 100, indicating how well the person has recovered.
    """
    # Initialize Recovery_Score with a base value
    df['Recovery_Score'] = 50

    # Adjust score based on Sleep_Hours
    # More than 7 hours of sleep improves recovery score by 20 points
    df.loc[df['Sleep_Hours'] >= 7, 'Recovery_Score'] += 20
    # Less than 6 hours of sleep reduces recovery score by 30 points
    df.loc[df['Sleep_Hours'] < 6, 'Recovery_Score'] -= 30

    # Adjust score based on Heart_Rate_bpm
    # Lower heart rate improves recovery score, higher worsens it
    df['Recovery_Score'] -= (df['Heart_Rate_bpm'] - 50) * 0.2

    # Adjust score based on Steps
    # More than 12000 steps reduce recovery score slightly due to potential strain
    df.loc[df['Steps'] > 12000, 'Recovery_Score'] -= 10

    # Ensure scores are within 0 to 100 range
    df['Recovery_Score'] = df['Recovery_Score'].clip(lower=0, upper=100)

    return df

def process_data():
    df = load_data()
    df = calculate_recovery_score(df)
    return df

