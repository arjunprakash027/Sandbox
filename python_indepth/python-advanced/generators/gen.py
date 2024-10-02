#gen.py

from time import sleep
from typing import Any

##############################
#this function in its raw form take 5 sec to run, even if you only care about 1st value or 3 values. And it takes the entire space even if we only partially need the values and not the entire value
#this is called eager function
def compute():
    rv = []

    for i in range(10):
        sleep(.5)
        rv.append(i)
    
    return rv
##############################

##############################
#one better way to do this is using generators
class Compute:

    #this is the normal eager method
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        rv = []

        for i in range(10):
            sleep(.5)
            rv.append(i)
        
        return rv

    #using generators
    def __iter__(self): 
        self.last = 0
        return self #self is considerted as valid itratable return value as self has __next__ implemented.

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv


c = Compute()
##############################

##############################
#now the above complex class can be easily modeled using yield statement
def compute_yield():
    for i in range(10):
        sleep(.5)
        yield i #the beautiful thing about yield is it gives the value as well as control back to user until next step of itration is run, ie it is a coroutine
##############################
 
##############################
# mental model on how to use generators properly for interving the code
# say we have 3 functions first,secound and third that must be run in sequence else all hells let loose.
# but we need to interleave them to have the best possible optimization at our disposal, thats when we use generators
def first(): pass
def secound(): pass
def third(): pass

def api():
    first()
    yield
    secound()
    yield
    third()
##############################
