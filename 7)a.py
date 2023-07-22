class Stack:
    def __init__(self):
        self.stack =[]
        print()
    def push(self,item):
        self.stack.append(item)
        print("Pushed ",item)
        print()

    def pop(self):
        if not self.empty():
            item = self.stack.pop()
            print(f"Popped {item}")
            print()

        else:
            print("Stack is empty")
            print()

    def empty(self):
        return len(self.stack)==0
    def display(self):
        print(self.stack)
        print()

class Queue:
    def __init__(self):
        self.queue =[]
    def enque(self,item):
        self.queue.append(item)
        print("enqued ",item)
        print()

    def deque(self):
        if not self.empty():
            item = self.queue.pop(0)
            print(f"Dequeud {item}")
            print()

        else:
            print("Queue is empty")
            print()

    def empty(self):
        return len(self.queue)==0
    def display(self):
        print(self.queue)
        print()

stack = Stack()
queue = Queue()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

stack.display()

stack.pop()
stack.pop()
stack.pop()
stack.pop()

stack.display()

stack.pop()
stack.pop()
stack.pop()
stack.pop()

queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
queue.enque(6)

queue.display()

queue.deque()
queue.deque()
queue.deque()
queue.deque()

queue.display()

queue.deque()
queue.deque()
queue.deque()
queue.deque()