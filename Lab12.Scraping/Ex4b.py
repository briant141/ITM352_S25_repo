from sodapy import Socrata
import pandas as pd

# Create a Socrata client
client = Socrata("data.cityofchicago.org", None)  # 'None' = no app token required for basic use

# Get JSON data from dataset "rr23-ymwb" with limit of 500 records
results = client.get("rr23-ymwb", limit=500)

# Convert to DataFrame
df = pd.DataFrame.from_records(results)

# (a) Inspect first few results
print(df.head())

# Print vehicles and fuel sources
print(df[['vehicle_make', 'vehicle_fuel_source']])





