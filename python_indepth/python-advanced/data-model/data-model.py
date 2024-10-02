#playing with dunder methods (data model methods)

class polynomial:

    def __init__(self,*coefs:int) -> None:
        self.coefs = coefs
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}*({self.coefs})'

    def __add__(self,other):
        return self.__class__(*(x+y for x,y in zip(self.coefs,other.coefs)))
    
p1 = polynomial(1,2,3)
p2 = polynomial(4,6,7)



