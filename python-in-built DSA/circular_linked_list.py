class Node:
    def __init__(self, data):
        self.ref = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_starting(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
        else:
            new_node.ref = self.head
            temp = self.head
            while(temp.ref != self.head):
                temp = temp.ref
            temp.ref = new_node
            self.head = new_node
    
    def print_ll(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while True:
                print(n.data, "->", end=" ")
                n = n.ref
                if n == self.head:  # Stop when we reach head again
                    break
            print()

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
        else:
            temp = self.head
            while(temp.ref != self.head):
                temp = temp.ref
            new_node.ref = self.head
            temp.ref = new_node
    
    def add_after(self, value, data):
        new_node = Node(data)
        if self.head is None:
            new_node.ref = new_node
            self.head = new_node
        elif self.head.data == value:
            self.head.ref = new_node
            new_node.ref = self.head
        else:
            temp = self.head.ref
            while(temp != self.head):
                temp = temp.ref
                if temp.data == value:
                    new_node.ref = temp.ref
                    temp.ref = new_node
            print("Value not found")

    def add_before(self, value, data):
        new_node = Node(data)
        if self.head is None:
            return 
        if self.head.data == value:
            temp = self.head
            while temp.ref != self.head:
                temp = temp.ref
            temp.ref = new_node
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            prev = self.head
            temp = self.head.ref
            while temp != self.head:
                if temp.data == value:
                    new_node.ref = temp
                    prev.ref = new_node
                    return
                prev = temp
                temp = temp.ref


obj1 = CircularLinkedList()
obj1.add_starting(40)
obj1.add_starting(30)
obj1.add_starting(20)
obj1.add_starting(10)
obj1.add_last(50)
obj1.add_starting(0.1)
obj1.add_after(30, 35)
obj1.add_before(40, 37)
obj1.print_ll()