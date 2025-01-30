# Asking the user to enter their birth year and turning the input into an integer 
birthyear = int(input("Please enter your birth year (four digits): "))

# The calculation of your age with the current year and birth year
age = 2025 - birthyear  #You can manually change 2025 for a different year

# The results of your age in 2025. We used the f string in class which makes it easier so we don't need to use the + and str
print(f"You were born in {birthyear} and your age in 2025 will be {age}")