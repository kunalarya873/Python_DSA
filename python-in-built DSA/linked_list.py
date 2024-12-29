class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_starting(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, " --> ", end="")
                n = n.ref
            print("None")

obj1 = LinkedList()
obj1.add_starting(10)
obj1.add_starting(20)
obj1.add_starting(30)
obj1.print()