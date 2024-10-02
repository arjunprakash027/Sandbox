#context.py

from sqlite3 import connect
from typing import Any

######################
# a very simple user context manager
with connect('test.db') as conn:
    cur = conn.cursor()
    cur.execute('create table point (x int, y int)')
    cur.execute('insert into point (x,y) values (1,2)')
    cur.execute('insert into point (x,y) values (4,6)')
    for row in cur.execute('select * from point'):
        print(row)
    cur.execute('drop table point') #there is another create and delete here, that is creating and deleting the database
######################

######################
# Doing the same but with temp table context manager
class temptable:
    def __init__(self,cur) -> None:
        self.cur = cur
    def __enter__(self):
        self.cur.execute('create table point (x int, y int)')
    def __exit__(self,*args):
        self.cur.execute('drop table point')

with connect('test.db') as conn:
    cur = conn.cursor()

    with temptable(cur):
        cur.execute('insert into point (x,y) values (1,2)')
        cur.execute('insert into point (x,y) values (4,6)')
        for row in cur.execute('select * from point'):
            print(row)
######################

######################
# Doing the same but with temp table context manager and generators
class contextmanagerUserDefined:
    def __init__(self,gen) -> None:
        self.gen = gen
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        self.args,self.kwargs = args,kwds
        return self
    def __enter__(self):    
        self.gen_ins = self.gen(*self.args,**self.kwargs)
        next(self.gen_ins)  
    def __exit__(self,*args):
        next(self.gen_ins,None) #None is for graceful ending instead of raising an expection

@contextmanagerUserDefined
def temptable_function(cur): #also represetned as contextmanagerUserDefined(temptable_function)
    cur.execute('create table point (x int, y int)')
    yield
    cur.execute('drop table point')

with connect('test.db') as conn:
    cur = conn.cursor()

    with temptable_function(cur):
        cur.execute('insert into point (x,y) values (1,2)')
        cur.execute('insert into point (x,y) values (4,6)')
        for row in cur.execute('select * from point'):
            print(row)
######################

######################
# Whatever we did above, can we easily done using contextlib

from contextlib import contextmanager

@contextmanager
def temptable_function(cur):
    cur.execute('create table point (x int, y int)')

    try:
        yield
    finally:
        cur.execute('drop table point')

with connect('test.db') as conn:
    cur = conn.cursor()

    with temptable_function(cur):
        cur.execute('insert into point (x,y) values (1,2)')
        cur.execute('insert into point (x,y) values (4,6)')
        for row in cur.execute('select * from point'):
            print(row)
######################