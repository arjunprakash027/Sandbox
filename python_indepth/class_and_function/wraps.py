import time

def findtime(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end=time.time()
        print (f"time taken to execute {func.__name__} is {end-start} seconds")
    return wrapper


