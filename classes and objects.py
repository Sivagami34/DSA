class Fruits:
    def __init__(self, name, colour, size, taste, preference):
        self.name = name
        self.colour = colour
        self.size = size
        self.taste = taste
        self.preference = preference
        
    def detail(self):
        print("I am ", self.colour, "in colour", "I am ", self.name, "I am ", self.size, "in size", "I taste ", self.taste, "My preference on your list is ", self.preference)

    def pref(self):
        self.preference = self.preference - 1

fruit = Fruits("apple", "red", "small", "sweet", 2)
fruitt = Fruits("banana", "yellow", "medium", "sweet", 4)
fruit.detail()
fruitt.detail()
fruitt.pref()
fruitt.detail()