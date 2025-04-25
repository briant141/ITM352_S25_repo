import matplotlib.pyplot as plt
import pandas as pd
import json
from matplotlib.ticker import MaxNLocator

# Load JSON data
with open('Trips from area 8.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert trip_miles to numeric, coerce errors to NaN
df['trip_miles'] = pd.to_numeric(df['trip_miles'], errors='coerce')

# Show rows before dropping NaN
print("Rows before dropping NaN:", len(df))

# Drop rows with NaN in trip_miles
df = df.dropna(subset=['trip_miles'])

# Show rows after dropping NaN
print("Rows after dropping NaN:", len(df))

# Filter trips >= 2 miles
df_filtered = df[df['trip_miles'] >= 2]

# Show rows after filtering
print("Rows after filtering trips >= 2 miles:", len(df_filtered))

# Round fares to 1 decimal place to reduce x-axis clutter
df_filtered['fare'] = pd.to_numeric(df_filtered['fare'], errors='coerce').round(1)

# Extract fare and trip_miles
fare = df_filtered['fare']
trip_miles = df_filtered['trip_miles']

# Plot
plt.figure(figsize=(10,6))
plt.scatter(fare, trip_miles, color='purple', alpha=0.5)
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.title('Fares vs Trip Miles (Filtered Trips >= 2 miles)')

# Control x-axis ticks
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(nbins=10))  # Limit x-ticks

plt.tight_layout()
plt.savefig('FaresXmiles.png')
plt.close()
