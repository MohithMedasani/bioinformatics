"""
Exercise 9


1) Write a decorator function that prints the:
     - real world time taken to run the function,
     - process time used to run the function, and
     - size of the return value (using sys.getsizeof())

2) Apply this decorator to the following functions:
    for_loop() - Create an empty list and append the values 1 to 1,000,000 to the list using a for loop
    list_comp() - Use list comprehension to create a list of all values 1 to 1,000,000
    numpy_list() - Create a numpy array with all values 1 to 1,000,000
    pandas_list() - Create a pandas data frame with all values 1 to 1,000,000
    generator_list() - Use generator comprehension to create a generator of the values 1 to 1,000,000
                (generator comprehension is the same as list comprehension, but uses () instead of [])

3) For each function in #2, write a new function that produces the log10 of every number from 1 to 1,000,000.
    for_loop_log()
    list_com_log()
    numpy_list_log()
    pandas_list_log()
    generator_list_log()

There are many different ways to complete this assignment and there is not one single best way that I would prefer.
The purpose of this exercise is to practice implementing a decorator function and gain experience and knowlege of
several different modules. As long as your submission does not circumvent the purpose of this exercise and completes
tasks 1, 2 and 3, then you will receive full credit.
"""

import sys
import numpy
import pandas
import time
import math


def time_decorator(my_def):

    def internal_wrapper(*args):
        t1 = time.time()
        t2 = time.process_time()
        def_result = my_def(*args)
        size = sys.getsizeof(def_result)
        t01 = time.time()
        t02 = time.process_time()
        print("'{}'finished in {} seconds,process time :{},size is{}".format(my_def.__name__,str((t01-t1)),str((t02-t2)),size))
        return def_result

    return internal_wrapper

@time_decorator
def first():
    return [x ** 2 for x in range(10000000)]
first()

@time_decorator
def for_loop():
    new_list = []
    for i in range(1000000):
        new_list.append(i)
for_loop()

@time_decorator
def for_loop_log():
    new_list = []
    for i in range(1000000):
        if i != 0:
            new_list.append(math.log10(i))
for_loop_log()

@time_decorator
def list_comp():
    numbers = [i for i in range(1000000)]
list_comp()

@time_decorator
def list_com_log():
    numbers = [x for x in range (1, 1000000)]
    return [math.log10(x) for x in numbers]
list_com_log()

@time_decorator
def numpy_list():
    array = numpy.arange(1,1000000)
numpy_list()

@time_decorator
def numpy_list_log():
    array = numpy.arange(1,1000000)
    temp = numpy.log10(array)
numpy_list_log()

@time_decorator
def pandas_list():
    array = numpy.arange(1, 1000000)
    array_2 = pandas.DataFrame(array)
pandas_list()

@time_decorator
def pandas_list_log():
    array = numpy.arange(1, 1000000)
    temp = numpy.log10(array)
    array_2 = pandas.DataFrame(temp)
pandas_list_log()

@time_decorator
def generator_list():
    new_list = (i for i in range(1000000))
generator_list()

@time_decorator
def generator_list_log():
    numbers = (x for x in range (1, 1000000))
    return (math.log10(x) for x in numbers)
generator_list_log()