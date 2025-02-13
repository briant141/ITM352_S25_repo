'''  
Define a list of survey response values (5, 7, 3, and 8) and store them in 
a variable. Next define a tuple of respondent ID values (1012, 1035, 1021, and 1053).
Use the .append() method to append the tuple to the list. Print out the list.  
'''

# we defined the survey response values using a variable and is a list (which is mutable, meaning you can change)
survey_responses = [5,7,3,8] # the bracket used here is called json, a javascript object notation

respondent_IDs = (1012, 1035, 1021, 1053) # we are creating a tuple, which is immutable. That means you cannot change it

a = [(1012,5),(1035,7)]

# appending the tuple to the list (adding the entire tuple as a single element)
survey_responses.append(respondent_IDs)

# print(mutant) there is nothing coming back, so we just need to print our survey responses

# prints out a list that contains the list from survey reponse, and the appended tuple 
print(survey_responses) 

# If we need to change the size, we can use a list and not a tuple