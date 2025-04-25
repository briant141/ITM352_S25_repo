import matplotlib.pyplot as plt
import pandas as pd
import json

# Load the JSON data
with open('Trips from area 8.json') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Extract fare and trip miles
fare = df['fare']
trip_miles = df['trip_miles']

# a. Scatter plot with plt.scatter()
plt.scatter(fare, trip_miles)
plt.title('Scatter Plot (plt.scatter)')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.show()

# b. Scatter plot with plt.plot (linestyle="none", marker=".")
plt.plot(fare, trip_miles, linestyle="none", marker=".")
plt.title('Scatter Plot (plt.plot)')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.show()

# c. Fancy scatter plot with marker="v", color="cyan", alpha=0.2
plt.plot(fare, trip_miles, linestyle="none", marker="v", color="cyan", alpha=0.2)
plt.title('Fancy Scatter Plot')
plt.xlabel('Fare')
plt.ylabel('Trip Miles')
plt.show()
