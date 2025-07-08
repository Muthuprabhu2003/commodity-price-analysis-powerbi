import pandas as pd

# Load CSV file
df = pd.read_csv("E:\powerbi\project\dataset.csv")

# Convert Arrival_Date to datetime
df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'], format='%d/%m/%Y')

# Basic check
print(df.info())
print(df.head())
