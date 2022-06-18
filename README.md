# Introduction to Higher Order Functions
A higher order function (HOF) is a function that takes one or more functions as arguments or return a function as a result, or both. They are supported by a wide range of programming languages including the most popular ones such as Python, C++ and JavaScript.

An example of Higher Order Functions that typically built-in within programming languages are:

map
fold
filter
Although they are simple concepts, knowing how to use them can very much improve the way you write code :). So let’s get started!

In this tutorial we’ll use Python, without any loss of generalization the same concepts apply to any other language.

# 1. map

The signature of map function in Python is map(function, iterable,)

map operates on iterables (lists, tuples, strings or any sequence that can be iterated on with a for loop)

map is used to apply a function to each item in the iterable, or in other words to map each item to something else.

Example: Let’s say we have this list of numbers, and we would to return zero for each negative number, and return the square of each positive number.
```
import math

list_of_nums = [1, 5, 10, -5, 8, -4, 3]

def my_function(x):
    if x < 0:
        return 0
    else:
        return math.pow(x, 2)

new_list_of_nums = list(map(my_function, list_of_nums))

print(new_list_of_nums)

#Output: [1, 25, 100, 0, 64, 0, 9]
```

# 2. reduce
reduce is the Pythonic version of foldl in Functional Programming, it can be used to apply operations that can accumulate the iterable, such as summing numbers, or concatenation of strings.

The reduce in Python is available in the functools module

The signature of reduce function in Python is reduce(function, iterable)

In reduce, the function we apply must have two arguments. This time we’ll use a lambda,

A lambda is an anonymous function that has the following syntax: lambda arguments : expression

In the following example, we are finding the sum of the first 100 natural numbers, the way this works is as follows it starts from the first item of the list from left to right:  ((((1+2)+3)+4)+5)...+100) = 5050

```
import functools

list_of_nums = list(range(1, 101))

sum_of_nums = functools.reduce(lambda x, y: x + y, list_of_nums)

print(sum_of_nums)

#Output: 5050
```

# 3. filter
The filter function as the name suggests, filters an iterable based on the boolean value returned by the function we pass.

The signature of filter function in Python is filter(function, iterable)

In the following example, we are filtering the list such that lowercase characters are removed.
```
list_of_chars= ['A','B','c','D','e','F',]

filtered_list = list(filter(lambda x: x.isupper(), list_of_chars))

print(filtered_list)

#Output: ['A', 'B', 'D', 'F']
```
