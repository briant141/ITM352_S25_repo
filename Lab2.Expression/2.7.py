# Asking the user input
fahrenheit_str = input("Enter the temperature in Fahrenheit: ")

#the try will help us convert the input string into a float
try:
    fahrenheit = float(fahrenheit_str)  #Converting the input to float
    celsius = (fahrenheit - 32) * (5/9) #Calculating celcius	        
    print(f"{fahrenheit} degree Fahrenheit is equal to {celsius} degree Celsius")

# Handling invalid inputs
except ValueError:
    print("Invalid input. Please enter a valid number for Fahrenheit.")








