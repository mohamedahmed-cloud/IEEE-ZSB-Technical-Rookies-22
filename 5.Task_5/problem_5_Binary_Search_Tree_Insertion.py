class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)
# Start of my code ##########################################################################
    def insert(self, val):
        #Enter you code here.
        if self.root is None:
            self.root=Node(val)
        else:
            key=self.root
            while True:
                if key.info >val:
                    if key.left is None:
                        key.left=Node(val)
                        break
                    else:
                        key=key.left
                else:
                    if key.right is None:
                        key.right=Node(val)
                        break
                    else:
                        key=key.right
# End of my code ##########################################################################

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)