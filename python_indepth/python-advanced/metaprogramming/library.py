
#creating a metaclass
class Basemeta(type):
    def __new__(cls,name,bases,body):

        if name != 'Base' and not 'bar' in body:
            raise TypeError("Bad type")
        print(cls,name,bases,body)
        return super().__new__(cls,name,bases,body)

class Base():
    def foo(self):
        return 'foo'
    
    def __init_subclass__(cls,*a,**kw) -> None:
        print("init subclass",cls,a,kw)
        cls.new_var = 23 #example modification to the derived class
        return super().__init_subclass__(*a,**kw)


# swapping default class building method with my own class building method

# old_bc = __build_class__

# def new_bc(fun,name,base=None,**kw):
#     print("New BC implemented:",fun,name,base)
#     if base:
#         return old_bc(fun,name,base,**kw)
#     return old_bc(fun,name,**kw)

# import builtins

# builtins.__build_class__ = new_bc
