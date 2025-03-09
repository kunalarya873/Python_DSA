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
    
    def delete(self, root, key):
        if not root:
            return root
        elif key < root.data:
            root.lchild = self.delete(root.lchild, key)
        elif key > root.data:
            root.rchild = self.delete(root.rchild, key)
        else:
            if root.lchild is None:
                temp = root.rchild
                root = None
                return temp
            elif root.rchild is None:
                temp = root.lchild
                root = None
                return temp
            temp = self.getMinValue(root.rchild)
            root.data = temp.data
            root.right = self.delete(root.rchild, temp.data)
        
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.lchild), self.getHeight(root.rchild))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.lchild) >= 0:
            return self.clockwiserotation(root)
        
        if balance > 1 and self.getBalance(root.lchild) <= 0:
            root.lchild = self.anticlockwiserotation(root.lchild)
            return self.anticlockwiserotation(root)
        
        if balance < 1 and self.getBalance(root.rchild) <= 0:
            return self.clockwiserotation(root)
        
        if balance < 1 and self.getBalance(root.rchild) > 0:
            root.rchild = self.anticlockwiserotation(root.rchild)
            return self.clockwiserotation(root)

        return root

        
    def getMinValue(self, root):
        if root is None or root.lchild is None:
            return None
        return self.getMinValue(root.lchild)


# 🌳 Creating the AVL Tree
mytree = AVL_tree()
root = None
values = [9, 4, 8, 6, 11, 16, 1, 2]

for val in values:
    root = mytree.insert(root, val)

print("Preorder of AVL tree:", end=" ")
mytree.preorder(root)
print()
mytree.delete(root, 16)
mytree.preorder(root)
print()
