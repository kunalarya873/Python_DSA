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
        
        # Insert in the correct subtree
        if key < root.data:
            root.lchild = self.insert(root.lchild, key)
        else:
            root.rchild = self.insert(root.rchild, key)

        # Update height of the node
        root.height = 1 + max(self.getHeight(root.lchild), self.getHeight(root.rchild))

        # Get balance factor
        balance = self.getBalance(root)

        # 🔹 Case 1: **Left Heavy (Right Rotation)**
        if balance > 1 and key < root.lchild.data:
            return self.clockwiserotation(root)

        # 🔹 Case 2: **Right Heavy (Left Rotation)**
        if balance < -1 and key > root.rchild.data:
            return self.anticlockwiserotation(root)

        # 🔹 Case 3: **Left-Right Case (Left Rotation + Right Rotation)**
        if balance > 1 and key > root.lchild.data:
            root.lchild = self.anticlockwiserotation(root.lchild)
            return self.clockwiserotation(root)

        # 🔹 Case 4: **Right-Left Case (Right Rotation + Left Rotation)**
        if balance < -1 and key < root.rchild.data:
            root.rchild = self.clockwiserotation(root.rchild)
            return self.anticlockwiserotation(root)

        return root

    def clockwiserotation(self, ptr1):
        temp2 = ptr1.lchild
        temp3 = temp2.rchild

        # Perform rotation
        temp2.rchild = ptr1
        ptr1.lchild = temp3

        # Update heights
        ptr1.height = 1 + max(self.getHeight(ptr1.lchild), self.getHeight(ptr1.rchild))
        temp2.height = 1 + max(self.getHeight(temp2.lchild), self.getHeight(temp2.rchild))

        return temp2  # New root after rotation

    def anticlockwiserotation(self, ptr1):
        temp2 = ptr1.rchild
        temp3 = temp2.lchild

        # Perform rotation
        temp2.lchild = ptr1
        ptr1.rchild = temp3

        # Update heights
        ptr1.height = 1 + max(self.getHeight(ptr1.lchild), self.getHeight(ptr1.rchild))
        temp2.height = 1 + max(self.getHeight(temp2.lchild), self.getHeight(temp2.rchild))

        return temp2  # New root after rotation

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.lchild) - self.getHeight(root.rchild)

    def preorder(self, root):
        if not root:
            return
        print(root.data, end=" ")
        self.preorder(root.lchild)
        self.preorder(root.rchild)


# 🌳 Creating the AVL Tree
mytree = AVL_tree()
root = None
values = [9, 4, 8, 6, 11, 16, 1, 2]

for val in values:
    root = mytree.insert(root, val)

print("Preorder of AVL tree:", end=" ")
mytree.preorder(root)
print()
