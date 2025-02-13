# Asking the users to input their first name, middle initial, and last name
first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')
	
# Creating a variable using f-strings (easier to do IMO compared to concatenate)
full_name = f"{first_name} {middle_initial} {last_name}"
	
# The result of what we got with our full_name using f-string
print(f"Your full name is {full_name}")
