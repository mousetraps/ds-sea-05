### COMPREHENSIONS ###

# 1. for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num**3)

# equivalent list comprehension
cubes = [num**3 for num in nums]    # [1, 8, 27, 64, 125]

# 2. for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num**3 for num in nums if num % 2 == 0]    # [8, 64]

# 3. for loop to cube even numbers and square odd numbers
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num**3)
    else:
        cubes_and_squares.append(num**2)

# equivalent list comprehension (using a ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]    # [1, 8, 9, 64, 25]

# 4. for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)

# equivalent list comprehension
items = [item for row in matrix
              for item in row]      # [1, 2, 3, 4]

# set comprehension 
fruits = ['apple', 'banana', 'cherry']
unique_lengths = [len(fruit) for fruit in fruits]   # {5, 6}

# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}              # {'apple': 5, 'banana': 6, 'cherry': 6}
fruit_indices = {fruit:index for index, fruit in enumerate(fruits)} # {'apple': 0, 'banana': 1, 'cherry': 2}



### MAP, REDUCE, FILTER ###

# 'map' applies a function to every element of a sequence and returns a list
simpsons = ['homer', 'marge', 'bart']
map(len, simpsons)                      # returns [5, 5, 4]
map(lambda word: word[-1], simpsons)    # returns ['r', 'e', 't']

# equivalent list comprehensions
[len(word) for word in simpsons]
[word[-1] for word in simpsons]

# 'reduce' applies a binary function to the first two elements of a sequence,
# then repeats with the result and the next element, through the end of the sequence
reduce(lambda x, y: x + y, range(4))    # (((0+1)+2)+3) = 6

# 'filter' returns a sequence containing the items from the original sequence
# for which the condition is True
filter(lambda x: x % 2 == 0, range(5))  # returns [0, 2, 4]



########Lambda############
def f (x): return x**2:
print f(8)

g = lambda x: x**2
print g(8)


def make_incrementor (n): return lambda x: x + n

f = make_incrementor(2)
g = make_incrementor(6)
print f(42), g(42)


nums = range(2, 50) 
for i in range(2, 8): 
    nums = filter(lambda x: x == i or x % i, nums)

print nums

sentence = 'It is raining cats and dogs'
words = sentence.split()
print words

lengths = map(lambda word: len(word), words)
print lengths


print map(lambda w: len(w), 'It is raining cats and dogs'.split())