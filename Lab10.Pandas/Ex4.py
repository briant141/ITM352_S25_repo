import pandas as pd
# Read the JSON file (assuming it's already downloaded locally as 'taxi_data.json')
url = "https://drive.google.com/uc?id=1-MpDUIRZxhFnN-rcDdJQMe_mcCSciaus"
df = pd.read_json(url)

# Print summary statistics
print(df.describe())
	
# Print the median for all numeric columns
print("\nMedian values:")
print(df['fare'].median())
