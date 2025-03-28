file_id = "1M-X_bypJJ6K5p6eM6aYBwt1qIizIiIex"
url = f'https://drive.google.com/uc?id={file_id}'

import pandas as pd
df = pd.read_csv(url)

df['units'] = pd.to_numeric(df['units'], errors='coerce')
df['sales_price'] = pd.to_numeric(df['sale_price'], errors='coerce')
df['land_sqft'] = pd.to_numeric(df['land_sqft'], errors='coerce')
df['gross_sqft'] = pd.to_numeric(df['gross_sqft'], errors='coerce')

# Filter rows with 500 or more units
filtered_df = df[df['units'] >= 500]

# Drop unnecessary columns
filtered_df = filtered_df.drop(columns=['id', 'easement', 'borough'])

# print(filtered_df.info())
print(filtered_df.head())