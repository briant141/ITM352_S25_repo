# Define ticket prices, these are our variables
normal_price = 14
senior_price = 8
tuesday_price = 10
matinee_price_senior = 5
matinee_price_regular = 8

# This is where users will input their age, the day of the week, and asking the matinee
your_age = int(input("Enter your age: "))
# This part is crucial for the later part of the code because we need that capitalizaiton
weekday = input("Enter the day of the week: ").capitalize()  # Normalize input, also the output will capitalize the first letter
matinee = input("Is it a matinee? (yes/no): ") == "yes"  # Converting to boolean

# This is here to determine the lowest applicable price
price = normal_price # Defaulting back to the normal price

# If statements over here!
if your_age >= 65 and matinee:
    price = matinee_price_senior
elif matinee:
    price = matinee_price_regular
elif matinee >= 65:
    price = min(price, senior_price)  # Senior discount
elif weekday == "Tuesday":
    price = min(price, tuesday_price)  # Tuesday discount

# Printing the final results
print(f"Age: {your_age}")
print(f"Day: {weekday}")
print(f"Matinee: {matinee}")
print(f"Final Ticket Price: ${price}")