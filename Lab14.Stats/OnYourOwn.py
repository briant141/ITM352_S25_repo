import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('taxi trips Fri 7_7_2017.csv')

# Create a pivot table counting trips between pickup and dropoff areas
pivot_table = pd.pivot_table(df, 
                             index='pickup_community_area', 
                             columns='dropoff_community_area', 
                             aggfunc='size', 
                             fill_value=0)

# Plot heatmap
plt.figure(figsize=(12,8))
sns.heatmap(pivot_table, cmap='Blues', annot=False)
plt.title('Heatmap of Taxi Trips (Pickup vs Dropoff Areas)')
plt.xlabel('Dropoff Community Area')
plt.ylabel('Pickup Community Area')
plt.tight_layout()
plt.show()
