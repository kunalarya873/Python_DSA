class Node:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
        self.height = 1

class AVL_tree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.data:
            root.lchild = self.insert(root.lchild.key)
        else:
            root.rchild = self.insert(root.rchild.key)
        root.height = 1 + max(self.getHeight(root.lchild), self.getHeight(root.rchild))
        balance = self.getBalance(root)
        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.lchild) - self.getHeight(root.rchild)
