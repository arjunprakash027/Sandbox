#decorators.py
from time import time

#the timer wraps around a function adding extra attributes to it, this is decorating a function

#the first section of code defines how decorators work in very basic sense
##
def timer(func):

    def f(x,y):
        before = time()
        rv = func(x,y)
        after = time()
        print("time taken:",after - before)
        return rv
    
    return f


def add(x,y):
    return x + y
add = timer(add)
##


#higher order decorators 
##
def repeat(times):
    def decorator(func):
        print(func)
        def wrapper(namen):
            for _ in range(times):
                result = func(name=namen)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet(namen="Alice")
##