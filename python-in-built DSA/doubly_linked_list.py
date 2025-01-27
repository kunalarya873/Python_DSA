class Node:
    def __init__ (self, data):
        self.pref = None
        self.data = data
        self.nref = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def add_starting(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
    
    def printdoublylinkedlist(self):
        if self.head is None:
            print("Linked List is empty")
        
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, " --> ", end="")
                temp = temp.nref
            print("None")
    
    def printdoublylinkedlistreverse(self):
        if self.head is None:
            print("Linked List is empty")
        
        else:
            temp = self.head
            while temp is not None:
                ptr = temp
                temp = temp.nref
            while ptr is not None:
                print(ptr.data, "-->", end="")
                ptr= ptr.pref
            print("None")
        
    
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.nref is not None:
                temp = temp.nref
            temp.nref = new_node
            new_node.pref = temp


obj1 = DoublyLinkedList()
obj1.printdoublylinkedlist()
obj1.add_starting(20)
obj1.add_starting(2000)
obj1.add_starting(210)
obj1.add_starting(1120)
obj1.add_end(333)
obj1.printdoublylinkedlist()
print()
obj1.printdoublylinkedlistreverse()
print()
