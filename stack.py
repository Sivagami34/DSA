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
            self.stack.pop()
        else:
            print("stack underflow")
    def top(self):
        return self.stack[len(self.stack)-1]
    def isempty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

fruit = Stack(3)
fruit.display()
fruit.push("kiwi")
fruit.display()
fruit.push("lemon")
fruit.display()
print(fruit.top())
fruit.push("apple")
fruit.display()
fruit.push("banana")
fruit.display()
fruit.pop()
fruit.display()
print(fruit.top())
