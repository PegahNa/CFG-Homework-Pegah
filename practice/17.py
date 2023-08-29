# sort out

"""
(A)
Given a list of integers, sort them out in descending order in place.
my_list = [3,6,8,5,7,85,4, 4,67,434,7]

(B)
Given a list of tuples, sort them by the second element in the tuple

tuples = [('apple', 3), ('pear', 5), ('banana', 1), ('lime', 4)]
output = [('banana', 1), ('apple', 3), ('lime', 4), ('pear', 5)]

"""

# A
my_list = [3, 6, 8, 5, 7, 85, 4, 4, 67, 434, 7]
print(sorted(my_list, reverse=True))

# B
tuples = [('apple', 3), ('pear', 5), ('banana', 1), ('lime', 4)]
print(sorted(tuples, key=lambda x: x[1]))

"""
(A)
Build a dictionary from a list of tuples. 
my_list = [('a', 1), ('b', 2)]

(B)
Use FOR loop to iterate through the dictionary and multiply each dic value 
by 5.
"""


# A
my_list = [('a', 1), ('b', 2)]
result = dict(my_list)


# B
for k, v in result.items():
   result[k] = v * 5

print(result)


