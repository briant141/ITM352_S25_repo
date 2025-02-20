# List of dictionaries where each of the dictionary represents a trip
trip_fares = [
    {'duration': 1.1, 'fare': '$6.25'},
    {'duration': 0.8, 'fare': '$5.25'},
    {'duration': 2.5, 'fare': '$10.50'},
    {'duration': 2.6, 'fare': '$8.05'}
    ]





# This what we are trying to go for, but in a easier more cleaner format
'''
[
    {'duration':1.1, 'fare': '$6.25'},
    {}
    
    ]
'''
# Printing out the duration and costs of the 3rd trip specifically, which is Index 2 because python follows a 0-based indexing
print(f"Duration: {trip_fares[2]['duration']} hours")
print(f'Cost: ${trip_fares[2]['fare']}' )
