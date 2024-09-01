class Queue:
    def __init__(self, max):
        self.max = max
        self.queue = []

    def enque(self, item):
        if self.size() < self.max:
            self.queue.append(item)
        else:
            print("queue overflow")
    
    def deque(self):
        if self.size() != 0:
            return self.queue.pop(0)
        else:
            print("queue underflow")

    def front(self):
        return self.queue[0]
    
    def rear(self):
        return self.queue[self.size() - 1]
    
    def display(self):
        print(self.queue)
    
    def size(self):
        return len(self.queue)

o = Queue(3)
o.enque(3)
o.display()
o.enque(4)
o.display()
print(o.front())
print(o.rear())
o.enque(2)
o.display()
o.enque(5)
o.display()
o.deque()
o.display()
print(o.front())
print(o.rear())
o.deque()
o.display()
o.deque()
o.display()
o.deque()
o.display()