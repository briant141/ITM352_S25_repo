# Given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Counter being initialized
string_counter = 0

# Loop through each element in the tuple
for item in data:
    if type(item) == str: # Checking if each element is a string
        string_counter += 1
        
        
print(f"There are {string_counter} strings in the tuple.")

