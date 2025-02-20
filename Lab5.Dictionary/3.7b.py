"""
Write Python code to define a list of taxi trip durations in miles (use values 1.1, 0.8, 2.5, 2.6). 
Also define a tuple of fares for the same number of trips (use values “$6.25,” “$5.25,” “$10.50,” “$8.05”). 
Store both the tuple and the list as values in a dictionary called trips, with keys “miles” and “fares.”
Print out the dictionary to show what it looks like.

"""
# List of trip durations and fares (durations mutable, fares not mutable)
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)
# A dictionary to store a trip data with the keys 'miles' and 'fares' 
trips = {
    'miles' : trip_durations,
    "fares":trip_fares
}
# Asking the user to type in a trip number 
trip_num = int(input('What trip do you want: '))
# Printing out the duration and fares of the trips, we converted the 1-based input to 0-based index
print(f'Duration: {trips['miles'][trip_num - 1]} hours' )
print(f'Cost: ${trips['fares'][trip_num - 1]}' )