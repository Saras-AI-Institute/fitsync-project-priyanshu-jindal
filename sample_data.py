import pandas as pd

def load_health_data(file_path):
    data = pd.read_csv(file_path)
    print("First 5 rows:")
    print(data.head())
    print("\nNumber of missing values in each column:")
    print(data.isnull().sum())

if __name__ == "__main__":
    load_health_data('data/health_data.csv')