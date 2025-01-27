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
        
    def delete_start(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
        elif self.head.ref is None:
            self.head = None
        else:
            temp = self.head
            ptr = temp.ref
            while ptr.ref is not None:
                temp = temp.ref
                ptr = ptr.ref
            temp.ref = None

    def delete_node(self, x):
        if self.head is None:
            print("Cannot be deleted")
        if x == self.head.data:
            self.head = self.head.ref
        temp = self.head
        while (temp.data != x):
            ptr = temp 
            temp = temp.ref
        if (temp is None):
            print("Node is not available")
        else:
            ptr.ref = temp.ref
            temp = None
    
    def delete_specific_node_after(self, x):
        if self.head == None:
            print("Cannot be Deleted")
            return
        temp = self.head
        while(temp.data != x):
            temp = temp.ref
            if (temp is None):
                print("Node is not available")
                return
        if temp.ref is None:
            print("Cannot be deleted")
            return
        elif(temp.ref.ref is None):
            ptr = temp.ref
            temp.ref = None
        else:
            ptr = temp.ref
            temp.ref = ptr.ref
            ptr = None
    
    def delete_specific_node_before(self, x):
        if self.head  == None:
            print("Can't delete the node")
            return
        temp = self.head
        ptr = temp.ref

        if (ptr is None or temp.data == x):
            print("can't be delete")
            return
        if ptr.data == x:
            self.head = temp.ref
            return
        if (ptr.ref is None):
            print("Node does not exist")
        while(ptr.ref.data !=x):
            ptr = ptr.ref
            temp = temp.ref
            if (temp.ref is None):
                print("Node does not exist")
                return
        temp.ref = ptr.ref
        ptr = None
        
        

obj1 = LinkedList()
obj1.add_starting(10)
obj1.add_starting(20)
obj1.add_starting(30)
obj1.add_end(40)
obj1.add_end(33)
obj1.add_after(100,30)
obj1.add_before(34,33)
obj1.print()
obj1.delete_start()
obj1.print()
obj1.delete_end()
obj1.print()
obj1.delete_node(40)
obj1.print()