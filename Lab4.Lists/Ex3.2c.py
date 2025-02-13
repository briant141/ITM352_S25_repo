# Asking the users to input their first name, middle initial, and last name
first_name = input('first name: ')
middle_initial = input('middle initial: ')
last_name = input('last name: ')

# Creating a variable using the %Operator (% operator allows us to have a finer degree of control)
full_name = "%s %s %s" % (first_name, middle_initial, last_name)

# The result of what we got with our full_name using %Operator
print(f"Your full name is %s" % full_name)

# Note the %s is like a placeholder for the string. Any object can be converted to string
# %s isn't the only operator there are more. 