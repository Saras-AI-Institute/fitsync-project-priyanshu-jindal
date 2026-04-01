import pandas as pd


def load_data():
    """
    Reads 'health_data.csv', handles missing values, converts date column, and returns a cleaned DataFrame.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv('data/health_data.csv')

    # Fill missing 'Steps' values with the median of that column
    df['Steps'].fillna(df['Steps'].median(), inplace=True)

    # Fill missing 'Sleep_Hours' values with a default value of 7.0
    df['Sleep_Hours'].fillna(7.0, inplace=True)

    # Fill missing 'Heart_Rate_bpm' values with a default value of 68
    df['Heart_Rate_bpm'].fillna(68, inplace=True)

    # Fill other missing values with the median of their respective columns
    df.fillna(df.median(), inplace=True)

    # Convert 'Date' column to datetime objects
    df['Date'] = pd.to_datetime(df['Date'])

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
