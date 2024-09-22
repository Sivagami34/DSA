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

def preorder(root):
    print(root.key)
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)

def postorder(root):
    if root.left is not None:
        postorder(root.left)
    if root.right is not None:
        postorder(root.right)
    print(root.key)

root = Node(6)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(7)
print("inorder: ")
inorder(root)
print("preorder: ")
preorder(root)
print("postorder: ")
postorder(root)
