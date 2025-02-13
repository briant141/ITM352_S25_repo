# Asking the users to input their first name, middle initial, and last name
first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')
	
# Storing the name components inside of a list 
name_components = [first_name, middle_initial, last_name]
 
# Using the format() and the * (unpacking) in order to insert the lists from above
full_name = "{} {} {}".format(*name_components)
	
# The result of what we got with format() and unpacking
print("Your full name is {}".format(full_name))