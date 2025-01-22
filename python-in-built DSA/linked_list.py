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
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.ref is not None:
                temp = temp.ref
            temp.ref = new_node
    
    def add_after(self, data, value):
        temp =self.head
        while temp is not None:
            if value == temp.data:
                break
            temp = temp.ref
        if temp is None:
            print("Node is not found in linked list")
        else:
            new_node = Node(data)
            new_node.ref = temp.ref
            temp.ref = new_node
    def add_before(self, data, value):
        if self.head is None:
            print("Linked list is emptyt")
        if self.head.data == value:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        temp = self.head
        while(temp.data != value):
            ptr = temp
            temp = temp.ref
        if temp is None:
            print("Node is not found is LL")
        else:
            new_node = Node(data)
            new_node.ref = ptr.ref
            ptr.ref = new_node


obj1 = LinkedList()
obj1.add_starting(10)
obj1.add_starting(20)
obj1.add_starting(30)
obj1.add_end(40)
obj1.add_end(33)
obj1.add_after(100,30)
obj1.add_before(34,33)
obj1.print()