# It will ask the user to enter a number from 1-100
user_input = input("Enter a number from 1-100:")

# This code will turn our input into a integer and will square the number of whatever the user inputted 
numbers = int(user_input)
Square = numbers * numbers

# The result of what number you put. It will show what number you put and then the square rooted
print("You put:", numbers)
print("The square root of that number is", Square)

# The code shown below is what we did in class with the professor. This is another way, and probably a efficient way as it doesn't need much lines to get us the same output as the code above.  
# user_input = int(input("Enter a number 1-100 ")) 
# print("The number you inputted is " + str(user_input) + " The square of " + str(user_input**2))