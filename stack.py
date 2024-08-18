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
        self.stack.pop()

fruit = Stack(3)
fruit.display()
fruit.push("kiwi")
fruit.display()
fruit.push("lemon")
fruit.display()
fruit.push("apple")
fruit.display()
fruit.push("banana")
fruit.display()
fruit.pop()
fruit.display()