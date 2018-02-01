"""
testing python, learning
"""

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

# List comprehension continued
X = [1, 2, 3, 4]
print([num ** 2 for num in X]) # instead of .append(num ** 2)

#function conventions
# snake case instead of camel case (javascript)
def my_func(param1 = 'default'):
    """
    This is the DOCSTRING
    """
    print(param1)

#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:

# arrayCheck([1, 1, 2, 3, 1]) → True
# arrayCheck([1, 1, 2, 4, 1]) → False
# arrayCheck([1, 1, 2, 1, 2, 3]) → True

def arrayCheck(nums):
    # CODE GOES HERE
    flag = False
    for num in nums:
        if num == 1:
            flag = True
        elif num == 2 and flag:
            flag = True
        elif num == 3 and flag:
            return True
        else:
            flag = False
    return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
    
    return str[::2]

print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))

#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
    lg_str = ''
    sm_str = ''
    if len(a) > len(b):
        lg_str = a
        sm_str = b
    else:
        lg_str = b
        sm_str = a
    return lg_str[len(lg_str) - len(sm_str):].lower() == sm_str.lower()

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  # CODE GOES HERE
    return ''.join([ch * 2 for ch in str])

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))


#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  # CODE GOES HERE
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c
def fix_teen(n):
  # CODE GOES HERE
    if n >= 13 and n <= 19:
        if n == 15 or n == 16:
            return n
        return 0
    return n

print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
