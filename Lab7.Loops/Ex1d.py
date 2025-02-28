'''odd_numbers = [2*num + 1 for num in range(0, 51) if 2*num + 1 <= 50] 

# Printing the final lists of odd numbers
for num in odd_numbers:
    print(num) '''
# This version above gives us in a veritcal list format, we did this in class

# Filtering odd numbers and using list comprehension in order to generate it
# Needing to combine both a loop and if condition on the same line
odd_numbers = [num for num in range(1, 51) if num % 2 != 0] 
print(odd_numbers) # this will print it out in a list