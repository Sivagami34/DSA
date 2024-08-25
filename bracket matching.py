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
        
def checkbracket(e):
    stack1 = Stack(5)
    open = ["(", "[", "{"]
    close = [")", "]", "}"]
    for c in e:
        if c in open:
            stack1.push(c)
        elif c in close:
            item = stack1.pop()
            if open.index(item) != close.index(c):
                return False
    if stack1.isempty():
        return True
    else:
        return False
print(checkbracket("(b+c)-a[a*c]+{b-a}"))
print(checkbracket("(b+c)-a[a*c]+{b]-a}"))
print(checkbracket("(b+c)-a[a*c+{b]-a}"))