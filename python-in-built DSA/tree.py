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
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data, end=" ")
    
    def search(self, value):
        if self.data == value:
            print("Node is Found")
            return
        if value < self.data:
            if self.lchild:
                self.lchild.search(value)
            else:
                print("Node does not exist")
        if value > self.data:
            if self.rchild:
                self.rchild.search(value)
            else:
                print("Node does not exist")

    def find_min(self):
        """Helper function to find the minimum node in a subtree."""
        node = self
        while node.lchild:
            node = node.lchild
        return node

    def delete(self, value):
        if self.data is None:
            print("Tree is empty")
            return
        if value < self.data:
            if self.lchild:
                self.lchild = self.lchild.delete(value)
            else:
                print("Node is not present in the tree")
        elif value > self.data:
            if self.rchild:
                self.rchild = self.rchild.delete(value)
            else:
                print("Node is not present in the tree")
        else:
            if self.lchild is None:
                return self.rchild
            if self.rchild is None:
                return self.lchild
            min_node = self.rchild.find_min()
            self.data = min_node.data  # Copy inorder successor's value
            self.rchild = self.rchild.delete(min_node.data)  # Delete the inorder successor
        return self

class BinarySearchTree:
    def __init__(self, data):
        self.val = data  # Renamed 'data' to 'val' for consistency
        self.left = None  # Changed from 'lchild' to 'left'
        self.right = None  # Changed from 'Rchild' to 'right'

    def insertvalue(self, value):
        if value < self.val:
            if self.left:
                self.left.insertvalue(value)
            else:
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insertvalue(value)
            else:
                self.right = BinarySearchTree(value)
def print_tree(root, val="val", left="left", right="right"):
    def display(root, val=val, left=left, right=right):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if getattr(root, right) is None and getattr(root, left) is None:
            line = '%s' % getattr(root, val)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if getattr(root, right) is None:
            lines, n, p, x = display(getattr(root, left))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
        if getattr(root, left) is None:
            lines, n, p, x = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = display(getattr(root, left))
        right, m, q, y = display(getattr(root, right))
        s = '%s' % getattr(root, val)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    lines, *_ = display(root, val, left, right)
    for line in lines:
        print(line)

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
print("Inorder Traversal of BST:", end=" ")
root.inorder_traversal()
print()
print("Preorder Traversal of BST:", end=" ")
root.preorder()
print()
print("Postorder Traversal", end=" ")
root.postorder()
print()
root.search(0)
root.delete(39)
root.inorder_traversal()
print()
# print_tree(root)
root = BinarySearchTree(10)
root.insertvalue(5)
root.insertvalue(15)
root.insertvalue(3)
root.insertvalue(7)
root.insertvalue(12)
root.insertvalue(18)

print_tree(root)