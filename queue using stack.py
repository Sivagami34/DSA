class Stack:
    def __init__(self, max):
        self.max = max
        self.stack = []
    def display(self):
        print(self.stack)
    def size(self):
        return len(self.stack)
    def push(self, value):
        if self.size() < self.max:
            self.stack.append(value)
        else:
            print("stack overflow")
    def pop(self):
        if not self.isempty(): 
            return self.stack.pop()
        else:
            print("stack underflow")
    def top(self):
        return self.stack[len(self.stack)-1]
    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self, max):
        self.max = max
        self.q = Stack(max)
        self.t = Stack(max)
    def enque(self, value):
        if self.q.size() < self.max:
            while self.q.size() > 0:
                item = self.q.pop()
                self.t.push(item)
            self.q.push(value)
            while self.t.size() > 0:
                item2 = self.t.pop()
                self.q.push(item2)
        else:
            print("Queue overflow")
    def deque(self):
        if not self.q.isempty():
            return self.q.pop()
    def display(self):
        self.q.display()

o = Queue(3)
o.enque(3)
o.display()
o.enque(4)
o.display()
o.enque(2)
o.display()
o.enque(5)
o.display()
o.deque()
o.display()
o.deque()
o.display()
o.deque()
o.display()
o.deque()
o.display()