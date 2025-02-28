'''Write code that will iterate through numbers from 1 to 10 
and print the number if it is not equal to 5 (using continue) 
and stop the loop entirely and print a message when it reaches 8 (using break).'''

for num in range(1,11): # gonna use a for loop just cause we already know what we want
    if num == 5:
        continue # means that it will skip this part of the loop for the rest of the iteration
    print(num) # This will print out the numbers before 8 (excluding 5)
    if num == 8:
        print("Number 8 has been reached, stopping loop.")
        break # exits the loop completely
    