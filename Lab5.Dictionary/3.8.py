# Tuples that contain survey responses and the correspondent IDs
survey_responses = (5, 7, 3, 8) # respondents giving their responses
respondent_IDs = (1012, 1035, 1021, 1053) # Unique IDs for eache element

# Making a dictionary that will map respondent IDs to their responses
responses = dict(zip(respondent_IDs, survey_responses))
# We decided to try to add another one to show it is easier
responses[1234] = 10
# Printing out the dictionary to show the final structure
print(responses)