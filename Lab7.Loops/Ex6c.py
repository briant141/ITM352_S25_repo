data = ("hello", 10, "goodbye", 3, "goodnight", 5)

user_value = input("Enter a value to append to the tuple: ")

# Doing try will not work, but will help us get a friendlier message of not working
try:
    data.append(user_value)
except AttributeError: # Had to use AI to find the attribute error
    print("Uh oh, Tuples cannot be changed and you can't change the value! :D ")