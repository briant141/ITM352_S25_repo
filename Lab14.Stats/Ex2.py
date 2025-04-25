import json
import os
import math
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
trips_data_filepath = os.path.join(current_dir, 'Trips from area 8.json')
with open(trips_data_filepath, 'r') as file:
    trips_data = json.load(file)
miles = [float(d['trip_miles']) for d in trips_data]

bins = int(math.sqrt(len(miles)))
plt.xlabel('Trip Miles')
plt.ylabel('Frequency')
plt.hist(miles, bins=bins, edgecolor='black')
plt.show()
