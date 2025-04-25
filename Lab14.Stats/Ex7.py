import matplotlib.pyplot as plt
import pandas as pd
import json
from mpl_toolkits.mplot3d import Axes3D  # 3D plotting

# Load JSON data
with open('Trips from area 8.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert trip_miles, fare, and dropoff_community_area to numeric
df['trip_miles'] = pd.to_numeric(df['trip_miles'], errors='coerce')
df['fare'] = pd.to_numeric(df['fare'], errors='coerce')
df['dropoff_community_area'] = pd.to_numeric(df['dropoff_community_area'], errors='coerce')

# Drop rows with NaN in trip_miles, fare, or dropoff_community_area
df = df.dropna(subset=['trip_miles', 'fare', 'dropoff_community_area'])

# Filter trips >= 2 miles
df_filtered = df[df['trip_miles'] >= 2]

# Extract variables
fare = df_filtered['fare']
trip_miles = df_filtered['trip_miles']
dropoff_area = df_filtered['dropoff_community_area']

# Create 3D plot
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(fare, trip_miles, dropoff_area, c='teal', marker='o', alpha=0.6)

# Labels
ax.set_xlabel('Fare')
ax.set_ylabel('Trip Miles')
ax.set_zlabel('Dropoff Community Area')
ax.set_title('3D Scatter Plot: Fare vs Trip Miles vs Dropoff Area')

plt.tight_layout()
plt.show()
