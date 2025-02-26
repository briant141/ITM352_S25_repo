# Define a list with different values (this can be modified for testing)

# listofstuff = [12, "hello", 10, True, None, 14]

# Test cases: Each list is representing a a different scenario
listofstuff = [
    [],                      # Case 1: Empty list (<5 elements)
    [1, 2],                  # Case 2: Fewer than 5 elements
    [1, 2, 3, 4, 5],         # Case 3: Exactly 5 elements (5-10 range)
    [1, 2, 3, 4, 5, 6, 7],   # Case 4: Between 5 and 10 elements
    list(range(11))
]

# Check the length of the list and print messages accordingly
if len(listofstuff) < 5:
    print("The list has fewer than 5 elements.")
elif 5 <= len(listofstuff) <= 10:
    print("The list has between 5 and 10 elements (inclusive).")
else:
    print("The list has more than 10 elements.")