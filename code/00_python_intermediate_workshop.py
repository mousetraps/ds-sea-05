'''
Python Intermediate Workshop
'''

'''
LISTS
'''

# creating
a = [1, 2, 3, 4, 5]     # create lists using brackets

# slicing
a[0]        # returns 1 (Python is zero indexed)
a[1:3]      # returns [2, 3] (inclusive of first index but exclusive of second)
a[-1]       # returns 5 (last element)

# appending
try:
    a[5] = 6        # error because you can't assign outside the existing range
except IndexError as err:
    print(err)

a.append(6)     # list method that appends 6 to the end
a = a + [0]     # use plus sign to combine lists

# checking length
len(a)      # returns 7

# checking type
type(a)     # returns list
type(a[0])  # returns int

# sorting
sorted(a)               # sorts the list
sorted(a, reverse=True) # reverse=True is an 'optional argument'
try:
    sorted(a, True)         # error because optional arguments must be named
except TypeError as err:
    print(err)

'''
STRINGS
'''

# creating
a = 'hello'     # can use single or double quotes

# slicing
a[0]        # returns 'h' (works like list slicing)
a[1:3]      # returns 'el'
a[-1]       # returns 'o'

# concatenating
a + ' there'        # use plus sign to combine strings
try:
    5 + ' there'        # error because they are different types
except Exception as err:
    print(err)
str(5) + ' there'   # cast 5 to a string in order for this to work

# uppercasing
try:
    a[0] = 'H'      # error because strings are immutable (can't overwrite characters)
except Exception as err:
    print(err)
a.upper()       # string method (this method doesn't exist for lists)

# checking length
len(a)      # returns 5 (number of characters)


'''
EXERCISE:
1. Create a list of the first names of your family members.
2. Print the name of the last person in the list.
3. Print the length of the name of the first person in the list.
4. Change one of the names from their real name to their nickname.
5. Append a new person to the list.
6. Change the name of the new person to lowercase using the string method 'lower'.
7. Sort the list in reverse alphabetical order.
Bonus: Sort the list by the length of the names (shortest to longest).
'''

family_members = ['Thing1', 'Thing3', 'Thing2']
print("1. created family members list:", family_members)

family_members_length = len(family_members)
if family_members_length > 0:
    print("2. name of last person in the list:", family_members[family_members_length-1])
    print("3. length of name of first person in list:", len(family_members[0]))

    family_members[0] = family_members[0].replace('thing', '<3')
    print("4. rename family member:", family_members)

    new_guy_suffix = family_members_length + 1
    family_members.append('Thing' + str(new_guy_suffix))
    print("5. added new guy:", family_members)

    family_members_last_index = len(family_members) - 1
    family_members[family_members_last_index] = family_members[family_members_last_index].lower()
    print("6. lowercase new guy:", family_members)

    family_members.sort()
    print("7. sort list in alphabetical order:", family_members)


'''
FOR LOOPS AND LIST COMPREHENSIONS
'''

# for loop to print 1 through 5
nums = range(1, 6)      # create a list of 1 through 5
for val in nums:        # num 'becomes' each list element for one loop
    print (val)

# for loop to print 1, 3, 5
other = [1, 3, 5]       # create a different list
for x in other:         # name 'x' does not matter, not defined in advance
    print (x)             # this loop only executes 3 times (not 5)

# for loop to create a list of 2, 4, 6, 8, 10
nums = range(1, 6)
doubled = []                # create empty list to store results
for num in nums:            # loop through nums (will execute 5 times)
    doubled.append(num*2)   # append the double of the current value of num


# equivalent list comprehension
doubled = [num*2 for num in nums]   # expression (num*2) goes first, brackets
                                    # indicate we are storing results in a list


'''
EXERCISE 1:
Given that: letters = ['a', 'b', 'c']
Write a list comprehension that returns: ['A', 'B', 'C']
'''


letters = ['a', 'b', 'c']
print(letters,'->', [x.capitalize() for x in letters])


'''
EXERCISE 2 (BONUS):
Given that: word = 'abc'
Write a list comprehension that returns: ['A', 'B', 'C']
'''

word = 'abc'
print(word, '->', [x.capitalize() for x in word])


'''
EXERCISE 3 (BONUS):
Given that: fruits = ['Apple', 'Banana', 'Cherry']
Write a list comprehension that returns: ['A', 'B', 'C']
'''

fruits = ['Apple', 'Banana', 'Cherry']

print(fruits, '->', [x[0] for x in fruits])


'''
DICTIONARIES
'''

# dictionaries are made of key-value pairs (like a real dictionary)
family = {'dad':'Homer', 'mom':'Marge', 'size':2}

# check the length
len(family)         # returns 3 (number of key-value pairs)

# use the key to look up a value (fast operation regardless of dictionary size)
family['dad']       # returns 'Homer'

# can't use a value to look up a key

try:
    family['Homer']     # error
except Exception as err:
    print(err)
    
try:
    # dictionaries are unordered
    family[0]           # error
except Exception as err:
    print(err)

# add a new entry
family['cat'] = 'snowball'

# keys must be unique, so this edits an existing entry
family['cat'] = 'snowball ii'

# delete an entry
del family['cat']

# keys can be strings or numbers or tuples, values can be any type
family['kids'] = ['bart', 'lisa']   # value can be a list

# accessing a list element within a dictionary
family['kids'][0]   # returns 'bart'

# useful methods
family.keys()       # returns list: ['dad', 'kids', 'mom', 'size']
family.values()     # returns list: ['Homer', ['bart', 'lisa'], 'Marge', 2]
family.items()      # returns list of tuples:
                    # [('dad', 'Homer'), ('kids', ['bart', 'lisa']), ('mom', 'Marge'), ('size', 2)]



#1. Print the name of the mom.

print(family['mom'])

#2. Change the size to 5.

family['size'] = 5
print(family['size'])

#3. Add 'Maggie' to the list of kids.

family['kids'].append('Maggie')
print(family['kids'])

#4. Fix 'bart' and 'lisa' so that the first letter is capitalized.
for idx, kid in enumerate(family['kids']):
    # kid = kid[0].capitalize() + kid[1:]
    family['kids'][idx] = kid[0].capitalize() + kid[1:]
    # family['kids'][idx] = kid

print(family['kids'])

#Bonus: Do this last step using a list comprehension.

family['kids'] = [x[0].lower() + x[1:] for x in family['kids']]
print(family['kids'])

'''
REQUESTS
'''

# import module (make its functions available)
import requests

print(requests)

# use requests to talk to the web
r = requests.get('http://www.google.com')
type(r)         # special 'response' object
r.text          # HTML of web page stored as string
type(r.text)    # string is encoded as unicode
r.text[0]       # string can be sliced like any string


'''
APIs

What is an API?
- Application Programming Interface
- Structured way to expose specific functionality and data access to users
- Web APIs usually follow the "REST" standard

How to interact with a REST API:
- Make a "request" to a specific URL (an "endpoint"), and get the data back in a "response"
- Most relevant request method for us is GET (other methods: POST, PUT, DELETE)
- Response is often JSON format
- Web console is sometimes available (allows you to explore an API)

API Providers: https://apigee.com/providers
Echo Nest API Console: https://apigee.com/console/echonest
API key: http://bit.ly/myechonest
'''

# request data from the Echo Nest API
r = requests.get('http://developer.echonest.com/api/v4/artist/top_hottt?api_key=KBGUPZPJZS9PHWNIN&format=json')
r.text          # looks like a dictionary
type(r.text)    # actually stored as a string
r.json()        # decodes JSON
type(r.json())  # JSON can be represented as a dictionary
top = r.json()  # store that dictionary

# store the artist data
artists = top['response']['artists']    # list of 15 dictionaries

# create a list of artist names only
names = [artist['name'] for artist in artists]  # can iterate through list to access dictionaries
