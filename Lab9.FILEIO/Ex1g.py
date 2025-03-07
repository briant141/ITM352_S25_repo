with open("names.txt", "a") as file:
    file.write("\nPort, Dan")  # Ensure it starts on a new line, that is what \n is for

# Open file in read mode and print the updated contents
with open("names.txt", "r") as file:
    print(file.read())  