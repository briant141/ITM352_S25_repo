import pandas as pd
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# Read the table from the Treasury site
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"
tables = pd.read_html(url)

# Grab the first table (or adjust index if needed)
df = tables[0]

# Print the 1 mo interest rates using .iterrows()
print("1-Month Interest Rates:")
for index, row in df.iterrows():
    print(row['1 Mo'])  # Make sure the column is exactly '1 Mo'
