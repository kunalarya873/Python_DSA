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
    
    def add_after(self, data, value):
        if self.head is None:
            print("Linked List is Empty")
        temp = self.head
        while(temp.data != value):
            temp = temp.nref
            if temp is None:
                print("Node is not found")
                return
        # Create new node and insert after the found node
        new_node = Node(data)
        new_node.pref = temp
        new_node.nref = temp.nref

        # If the node is not the last one, update the next node's previous pointer
        if temp.nref is not None:
            temp.nref.pref = new_node
        
        # Update the original node's next pointer
        temp.nref = new_node
    
    def add_before(self, data, value):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == value:
            new_node = Node(data)
            new_node.nref = self.head
            self.head.pref = new_node
            self.ead = new_node
            return
        temp = self.head
        while(temp.data != value):
            ptr = temp
            temp = temp.nref
            if temp is None:
                print("Node is not found")
                return
        new_node = Node(data)
        new_node.nref = temp
        new_node.pref = ptr
        ptr.nref = new_node
        temp.pref = new_node
    
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        else:
            temp = self.head
            self.head = temp.nref
            if temp.nref is not None:
                self.head.pref = None
    
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.nref is None:
            self.head = None
        else:
            temp = self.head
            ptr = temp.nref
            while ptr.nref is not None:
                temp = temp.nref
                ptr = ptr.nref
            temp.nref = None
            ptr = None
    
    def delete_specific(self, data):
        if self.head is None:
            print("Linked List is empty")
            return
        elif self.head.data == data:
            if self.head.nref is None:
                self.head = None
            else:
                self.head = self.head.nref
                self.head.pref = None
            return
        else:
            temp = self.head
            while temp is not None:
                if temp.data == data:
                    if temp.nref is not None:
                        temp.nref.pref = temp.pref
                    if temp.pref is not None:
                        temp.pref.nref = temp.nref
                    return
                temp = temp.nref
            print("Node not found")


obj1 = DoublyLinkedList()
obj1.printdoublylinkedlist()
obj1.add_starting(20)
obj1.add_starting(2000)
obj1.add_starting(210)
obj1.add_starting(1120)
obj1.add_end(333)
obj1.add_after(10,210)
obj1.add_before(123, 10)
obj1.printdoublylinkedlist()
obj1.delete_begin()
obj1.delete_end()
obj1.delete_specific(210)
obj1.printdoublylinkedlist()
print()
obj1.printdoublylinkedlistreverse()
print()
