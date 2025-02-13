# Asking the users to input their first name, middle initial, and last name
first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')
	
# Using the .join will help us concatenate the strings with a space separator 
full_name = " ".join([first_name, middle_initial, last_name])
	
# The result of what we got with our full_name using .join
print("Your full name is ", full_name)
