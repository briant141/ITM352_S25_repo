def midpoint(begin_point, end_point):
    return (begin_point + end_point) / 2

def squareroot(number):
    return (number**0.5)

def exponent(base, exponent):
    return(base**exponent) # 

def max_value(num1, num2):
    return(num1 > num2)*num1 + (num1 < num2)*num2

def min_value(num1, num2):
    return(num1 < num2)*num1 + (num1 > num2)*num2

def function_applied(x, y, func):
    return f"The function {func.__name__}({x}, {y}) = {func(x, y)}" #extra credit question

print("Handymath loading in...")
