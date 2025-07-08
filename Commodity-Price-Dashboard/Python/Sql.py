import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv("E:\powerbi\project\dataset.csv")
df['Arrival_Date'] = pd.to_datetime(df['Arrival_Date'], format='%d/%m/%Y')
print(df.info())
print(df.head())
engine = create_engine("mysql+mysqlconnector://veguser:vegpass@localhost/vegetable_db")
df.to_sql("vegetable_prices", con=engine, if_exists="replace", index=False)
print(" Enriched data uploaded to MySQL!")