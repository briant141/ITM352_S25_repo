import pandas as pd
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# URL to the Treasury page
url = "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202410"

# Read all tables from the page (requires lxml)
tables = pd.read_html(url)

# Check how many tables were found
print(f"Found {len(tables)} tables.")

# Let's assume the first one is the one we want
if tables:
    df = tables[0]
    # Print the DataFrame's column names
    print("Columns:", df.columns.tolist())

