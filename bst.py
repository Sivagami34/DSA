class Node():
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None

def inorder(root):
    if root.left is not None:
        inorder(root.left)
    print(root.key)
    if root.right is not None:
        inorder(root.right)

def insert(root, newvalue):
    if root is None:
        return Node(newvalue)
    if root.key < newvalue:
        root.right = insert(root.right, newvalue)
    else:
        root.left = insert(root.left, newvalue)
    return root

nnodes = int(input("How many nodes would you like to insert? "))
root = None
for i in range(nnodes):
    val = int(input("Enter a value: "))
    root = insert(root, val)
inorder(root)