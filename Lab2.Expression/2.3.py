#Asking the users to input a decimal number between 1-100
decimal_input = (input("Please enter a number between from 1-100 (Ex. 99.9): "))

#Creating a variable in order to convert the input into a float (float will allow us to have decimals)
decimalnumber = float(decimal_input)

# This variable creates a squared of the number that was inputted by the user
squarednumber = decimalnumber ** 2 

#Printing out the results and like what you did in class today, the f-string makes thing so much easier and cleaner
print(f"You entered {decimalnumber}, and the squared version is {squarednumber}")

