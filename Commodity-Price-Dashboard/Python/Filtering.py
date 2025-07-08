import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("E:\powerbi\project\dataset.csv")
df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'], format='%d/%m/%Y')
tomato_df = df[df['Commodity'].str.lower() == 'tomato']
trend = tomato_df.groupby('Arrival_Date')['Modal_Price'].mean().reset_index()
plt.figure(figsize=(10, 5))
plt.plot(trend['Arrival_Date'], trend['Modal_Price'], marker='o')
plt.title("Tomato Price Trend in Tamil Nadu Markets")
plt.xlabel("Date")
plt.ylabel("Average Modal Price (₹)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
