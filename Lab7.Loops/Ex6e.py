# Given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Getting the user input
user_value = input("Enter a value to append to the tuple: ")

# Use unpacking (*) to create a new tuple as it was asked in the problem
data = (*data, user_value)

# Print out the updated tuple results
print("Updated Tuple:", data)