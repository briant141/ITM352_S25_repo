# Writing a python code to define a list of taxi trip durations in miles
# list of trip durations in miles
trip_durations = [1.1, 0.8, 2.5, 2.6]
# list of trip fares in dollars
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Creating a dictionary using the zip() function 
# zip(trip_durations, trip_fares) pairs each duration with its corresponding fare
# dict() converts the zipped pairs into a dictionary
trips = dict(zip(trip_durations, trip_fares))

# Printing out the results
print(trips)