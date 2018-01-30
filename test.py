

# string interpolation
SOME_DOGS = "First Dog: {x} Second Dog: {y}".format(x="audio", y="notaudio")
print(SOME_DOGS)

#list comprehension
MATRIX = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
FIRST_COL = [row[0] for row in MATRIX]
print(FIRST_COL)

#dictionaries
MY_STUFF = {"key1": 123, 'key2': 'value2', 'key3': {'123':[1, 2, 'grabMe']}}
print(MY_STUFF['key3']['123'][2])

#tuples - like lists, but immutable
T = (1, 2, 3)


#Exercise overview for Number, Strings, Lists, Dictionaries, Tuples, Sets, and Booleans
S = 'django'
# Use indexing to print out the following:

#'d'
print(S[0])
#'o'
print(S[5])
#'djan'
print(S[:4])
#'jan'
print(S[1:4])
#'go'
print(S[4:])
#Bonus: use indexing to reverse the string
print(S[::-1])

#Given this nested list:
L = [3, 7, [1, 4, 'hello']]

#Reassign 'hello' to be 'goodbye'
L[2][2] = 'goodbye'
print(L)

# Using keys and indexing , grab the 'hello' from the following dictionaries:
D1 = {'simple key': 'hello'}
print("d1", D1['simple key'])
D2 = {'k1': {'k2': 'hello'}}
print("d2", D2['k1']['k2'])
D3 = {'k1': [{'nest_key':['this is deep', ['hello']]}]}
print("d3", D3['k1'][0]['nest_key'][1][0])

# Use a set to find the unique values of the list below:
MYLIST = [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
print(set(MYLIST))

# You are given two variables
AGE = 4
NAME = "Sammy"

print("Hello my dog's name is {x} and he is {y} years old".format(x=NAME, y=AGE))
