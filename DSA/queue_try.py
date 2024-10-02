arr = []

def enqueue(element) -> None:
    arr.append(element)

def dequeue() -> None:
    arr.pop(0)

def display() -> None:
    for i in arr:
        print(i, end = ' ')
    print()

enqueue(1)
enqueue(2)
enqueue(3)
display()
dequeue()
display()