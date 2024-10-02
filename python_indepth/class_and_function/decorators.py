#using function as a arguement

def add(x,y):
    return x+y
def sub(x,y):
    return abs(x-y)

def math(f,x,y):
    print("func as arguement:",f(x,y))

math(sub,20,40)

#returning a fucntion inside a function

def mathf(x,y):
    def add():
        return x+y
    def sub():
        return abs(x-y)
    return add,sub

a = mathf(20,40)
print("func inside a func:",a[1]())

#decorator useage 

def dec(func):

    def innerfunc():
        print("this is before the execution of the function")
        func()
        print("this is after the execution of a function")

    return innerfunc

def useage():
    print("running the function block")

dec(useage)()

#example 2
import time
import math

def calculatetime(func):
    
    def wrapper(*args,**kwargs):
        print("func starts")
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("time taken by the {} is: {}".format(func.__name__,end-start))
    return wrapper

@calculatetime
def factorial(n):
    print(math.factorial(n))

def anotherfac(n):
    print(math.factorial(n))

factorial(10)
anotherfac(10)

#memoization using decorators

memory = {}

def memoize_fact(func):
    def wrapper(*args,**kwargs):
        if args not in memory:
            memory[args] = func(*args,**kwargs)
            print("result saved to memory for {}".format(args))
        else:
            print("result already in memory for {}".format(args))
        return memory[args]
    
    return wrapper

@memoize_fact
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    

print(factorial(10))
print(factorial(5))
#print(factorial(25))
#print(factorial(40))
