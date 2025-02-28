# given tuple
data = ("hello", 10, "goodbye", 3, "goodnight", 5)

user_value = input("Enter a value to append to the tuple: ")

data.append(user_value)

print("The new tuple: ", data)

# this gives us an error due to the fact that we cannot append a tuple