# Asking the users to input their first name, middle initial, and last name
first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')
	
# Basically saying that in these braces, they are going to get replaced by the format values inside
# which is the first_name, middle_initial, and last_name
full_name = "{} {} {}".format(first_name, middle_initial, last_name)
	
# The result of what we got with our full_name using format()
print("Your full name is {}".format(full_name))
