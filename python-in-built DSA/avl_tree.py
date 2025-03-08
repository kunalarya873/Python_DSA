class Node:
    def __init__(self, data):
        self.data = data
        self.rchild = None
        self.lchild = None
        self.height = 1

class AVL_tree:
    def __init__(self):
        self.head = None
    
