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

obj1 = CircularLinkedList()
obj1.add_starting(10)
obj1.add_starting(20)
obj1.add_starting(30)
obj1.add_starting(40)
obj1.print_ll()