import requests

# URL for license counts by driver_type
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# Make GET request
response = requests.get(url)

# Convert to JSON
records = response.json()

# Print response
print(records)

# Shows us the type of data format it is
print(f"\nData format: {type(records)}") 
