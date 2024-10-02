class cq:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1
    
    def isfull(self):
        if len(self.items) == self.size - 1:
            return 1
        else:
            return 0
    def enque(self,data):
        if self.isfull():
            print("queue is full")
        elif(self.front == -1):
            self.front = 0
            self.rear = (self.rear+1) % self.size
            self.items[self.rear] = data
        else:
            self.rear = (self.rear+1)%self.size
            self.items[self.rear] = data
    
    def isempty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0

    def deque(self):
        if self.isempty():
            print("empty queue")
        elif (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front+1)%self.size

    def display(self):
        if (self.rear == -1):
            print("no element")
        elif (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.items[i], end = ' ')
            print()
        else:
            for i in range(self.front, self.size):
                print(self.items[i], end = ' ')
            for i in range(0, self.rear + 1):
                print(self.items[i], end = ' ')
            print()
    
queue = cq(5)
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.display()
queue.deque()
queue.deque()
queue.display()






