# we defined the survey response values using a variable and is a list
survey_responses = [5,7,3,8]

# Appending a new value, which is 0, to the list 
survey_responses.append(0)

# We are now inserting another new value which is 6, at the index of 2 (which is the 3rd position, it counts 0 that's why)
survey_responses.insert(2, 6)

# Printing out the results of our new added values in the list
print(survey_responses)