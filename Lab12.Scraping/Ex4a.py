from sodapy import Socrata
import pandas as pd

# Connect to the Chicago data portal
client = Socrata("data.cityofchicago.org", None)

# Fetch 500 records from the dataset
results = client.get("rr23-ymwb", limit=500)

# Convert to a DataFrame
df = pd.DataFrame.from_records(results)

# Show the first few rows
print(df.head())

