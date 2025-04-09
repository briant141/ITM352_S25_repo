import requests
import pandas as pd

# Make GET request to the API
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"
response = requests.get(url)

# Convert the JSON response to records
records = response.json()

# Convert records to DataFrame
df = pd.DataFrame(records)

# Rename 'count_license' to 'count' for clarity
df.rename(columns={'count_license': 'count'}, inplace=True)

# Convert count from string to integer
df['count'] = pd.to_numeric(df['count'])

# Set 'driver_type' as the index
df.set_index('driver_type', inplace=True)

# Print the final DataFrame
print(df)
