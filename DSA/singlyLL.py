#linked list is not a inbuilt data structure in python
#it is a linear data structure
#uses a node class to store data and a pointer to the next node

class node:
    def __init__(self,data):
        self.value = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printll(self):
        if self.head == None:
            print("empty list")
        else:
            n = self.head
            while n is not None:
                print(n.value)
                n = n.ref
    
    def remove(self,key):
        n = self.head
        if n is not None:
            if n.value == key:
                self.head = n.ref
                n = None
                return
        
        while n is not None:
            if n.value == key:
                break

            prev = n
            n = n.ref
        
        if (n == None) :
            return
        
        prev.ref = n.ref
        n = None
        



ll = linkedlist()
ll.head = node(10)
secound = node(30)
thired = node(40)
fourth = node(90)
fifth = node(239)

ll.head.ref = secound
secound.ref = thired
thired.ref = fourth
fourth.ref = fifth

ll.printll()

ll.remove(30)

ll.printll()