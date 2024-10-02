from library import Base

#How to make sure that code dosent break if the library developer removed the foo method

#method 1 (use assert)

assert hasattr(Base,'foo'), "Broke"

class Derived(Base):
    def bar(self):
        return self.foo()