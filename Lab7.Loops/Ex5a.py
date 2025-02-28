# Define tuples
celebrities_tuple = ("Robert Downey Jr.", "Cristiano Ronaldo", "Ella Purnell", "Keanu Reeves", "Sean Schemmel")
ages_tuple = (59, 40, 28, 60, 56)  # Adjusted ages

# Initialize lists
celebrities_list = []
ages_list = []

# Iterate through tuples and append values to lists
for celeb in celebrities_tuple:
    celebrities_list.append(celeb)

for age in ages_tuple:
    ages_list.append(age)

# Store lists in a dictionary
celebrities_dict = {
    "celebrities": celebrities_list,
    "ages": ages_list
}

# Print the result
print(celebrities_dict)