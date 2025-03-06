class BinaryST:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None  # Fixed naming

    def insertvalue(self, value):
        if value < self.data:  # Use "<" for left child
            if self.lchild:
                self.lchild.insertvalue(value)
            else:
                self.lchild = BinaryST(value)
        else:  # Use ">=" for right child
            if self.rchild:
                self.rchild.insertvalue(value)
            else:
                self.rchild = BinaryST(value)

    def inorder_traversal(self):  # Added traversal for testing
        if self.lchild:
            self.lchild.inorder_traversal()
        print(self.data, end=" ")
        if self.rchild:
            self.rchild.inorder_traversal()
    def preorder(self):
        print(self.data, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
# Create the root node
root = BinaryST(10)
print("Root:", root.data)

# Insert values
root.insertvalue(39)
root.insertvalue(5)
root.insertvalue(20)
root.insertvalue(1)

# Print children properly
print("Left child of root:", root.lchild.data if root.lchild else None)
print("Right child of root:", root.rchild.data if root.rchild else None)

# Inorder traversal to verify correctness
print("Inorder Traversal of BST:")
root.inorder_traversal()
print()
root.preorder()
print()
