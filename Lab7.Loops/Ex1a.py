odd_numbers = []  # Creating an empty list that will soon be used to store odd numbers

for num in range(1, 51):  # Loop from 1 to 50
    if num % 2 != 0:  # Checking if the number is odd, also != means not equal
        odd_numbers.append(num)  # Adding the odd numbers to the list

# Printing the output of any odd numbers that was added
print(odd_numbers)