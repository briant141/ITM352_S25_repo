# we defined the survey response values using a variable and is a list
survey_responses = [5,7,3,8]

# Add the response "0' to the end of the list using the slice method and also the +
survey_responses = survey_responses + [0] # Or responses += [0]

# Add the reponse "6" between 7 and 3 using the slicing and + method
survey_responses = survey_responses[:2] + [6]+ survey_responses[2:]

print(survey_responses)

# this is like the immutable way of doing it