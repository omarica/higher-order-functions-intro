'''
Map function
'''

import math

list_of_nums = [1, 5, 10, -5, 8, -4, 3]


def my_function(x):
    if x < 0:
        return 0
    else:
        return math.pow(x, 2)


new_list_of_nums = list(map(my_function, list_of_nums))

print(new_list_of_nums)

'''
Reduce function
'''

import functools

list_of_nums = list(range(1, 101))

sum_of_nums = functools.reduce(lambda x, y: x + y, list_of_nums)

print(sum_of_nums)

'''
Filter function
'''

list_of_chars = ['A','B','c','D','e','F',]

filtered_list = list(filter(lambda x: x.isupper(), list_of_chars))

print(filtered_list)