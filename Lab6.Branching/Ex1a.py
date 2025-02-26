# A tuple that will store different emotions (immutable)
emotions = ('happy', 'sad', 'fear', 'surprise')

# the () really help because due to the order of operations. So, it will check which one has the higher order
# Using an if statement, without having an IF statement shown below
# print( (len(emotions) > 3 and emotions[-1] == 'happy'))

# An alternative, print only if the last element is happy
#print( emotions[- 1] == 'happy')

if( (len(emotions) > 3 and emotions[-1] == 'happy') ):
    print('len is > 3 and last is happy')
    print('and some more stuff too')
else:
    print('len is not > 3 or last is not happy')