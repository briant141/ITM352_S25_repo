import pandas as pd
import numpy as np

# Format all float output as currency with 2 decimal places
pd.set_option('display.float_format', "${:,.2f}".format)
pd.set_option('display.max_columns', None)

url = 'https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K'

try:
    df = pd.read_csv(url, engine='pyarrow', on_bad_lines='skip')

    # Convert order_date to datetime
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    # Convert quantity and unit_price to numeric
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')

    # Compute sales
    df['sales'] = df['quantity'] * df['unit_price']

    # Create pivot table with both sum and average (mean)
    pivot_table = pd.pivot_table(
        df,
        values='sales',
        index='sales_region',
        columns='order_type',
        aggfunc=[np.sum, np.mean],  # Include both total and average
        margins=True,
        margins_name="Total Sales"
    )

    # Print the final pivot table
    print(pivot_table)

except Exception as e:
    print(f"Error reading the file: {e}")
