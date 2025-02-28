# Given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Get user input
user_value = input("Enter a value to append to the tuple: ")

# Recasting the tuple to a list so we can make changes
data_list = list(data)

# Use .append() (lists allow modification)
data_list.append(user_value)

# After the changes converting it back to tuple, as if nothing happened
data = tuple(data_list)

# Print updated tuple
print("Updated Tuple:", data)