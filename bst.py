
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

def search(root, value):
    if root.key == value:
        return True
    elif root.key < value and root.right is not None:
        return search(root.right, value)
    elif root.key > value and root.right is not None:
        return search(root.left, value)
    else:
        return False
    
def insucc(nnode):
    succ = nnode.right
    while succ.left is not None:
        succ = succ.left
    return succ

def delete(root, value):
    if root == None:
        return None
    if root.key < value:
        root.right = delete(root.right, value)
    elif root.key > value:
        root.left = delete(root.left, value)
    else:
        if root.right is None:
            return root.left
        if root.left is None:
            return root.right
        suc = insucc(root)
        root.key = suc.key
        root.right = delete(root.right, suc.key)
    return root

nnodes = int(input("How many nodes would you like to insert? "))
root = None
for i in range(nnodes):
    val = int(input("Enter a value: "))
    root = insert(root, val)
inorder(root)
print(search(root,8))
d = int(input("what node would you like to delete: "))
delete(root, d)
inorder(root)
