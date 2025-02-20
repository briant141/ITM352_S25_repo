# We made it into a dictionary, using the {}. 
trip_data = {
    "Trip_id": "da7a62fce",
    "Trip_seconds": 360,
    "Triple_miles": 1.1,
    "Fare": "$6.25"
}

print(trip_data) # prints out the same way, but we made it into a dictionary
                 # We know this because we put double quotes, but when printed out it gives us single quotes
print(f"Trip miles are {trip_data['Triple_miles']}")