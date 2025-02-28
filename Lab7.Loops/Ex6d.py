# Given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_value = input("Enter a value to append to the tuple: ")

# Manually create a new tuple with the additional value
new_data = tuple(list(data) + [user_value])  # Convert tuple to list, add value, convert back

# Print the updated tuple
print("The new tuple:", new_data)