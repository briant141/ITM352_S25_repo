"""
Write Python code to define a list of taxi trip durations in miles (use values 1.1, 0.8, 2.5, 2.6). 
Also define a tuple of fares for the same number of trips (use values “$6.25,” “$5.25,” “$10.50,” “$8.05”). 
Store both the tuple and the list as values in a dictionary called trips, with keys “miles” and “fares.”
Print out the dictionary to show what it looks like.

"""

# List of trip of durations in miles (mutable)
trip_durations = [1.1, 0.8, 2.5, 2.6]
# list of trip fares (not mutable)
trip_fares = ("$6.25", "$5.25", "$10.50", "$8.05")

# Creating a dictionary to store the trip dats with keys like 'miles' and 'fares'
trips = {
	"miles":trip_durations,
    "fares":trip_fares
    
    }

# Printing out the results of the dictionary, showing the final structures of it
print(trips)
