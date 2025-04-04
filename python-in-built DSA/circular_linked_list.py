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
            print("List is empty, cannot insert after a value")
            return
        temp = self.head
        while True:
            if temp.data == value:
                new_node.ref = temp.ref 
                temp.ref = new_node
                return
            temp = temp.ref
            if temp == self.head: 
                break
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

    def delete_start(self):
        if self.head is None:
            print("Linked list is empty")
        temp = self.head
        if temp.ref is self.head:
            self.head = None
            return
        second = temp.ref 
        while temp.ref != self.head:
            temp = temp.ref
        temp.ref = second
        self.head = second
        return

    def delete_end(self):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head.ref == self.head:
            self.head = None
            return
        prev = self.head
        temp = prev.ref
        while temp.ref != self.head:
            prev = temp
            temp = temp.ref
        prev.ref = self.head
        return

    def delete_specific(self, value):
        if self.head is None:
            print("Linked List is empty")
        prev = self.head
        if self.head.data == value:
            self.head = None
        temp = prev.ref
        while temp != self.head:
            prev = temp
            temp = temp.ref
            if temp.data == value:
                prev.ref = temp.ref
                return
        print("Node not found")

    def delete_after_specific(self, value):
        if self.head is None:
            print("Linked List is empty")
            return
        temp = self.head
        while True:
            if temp.data == value:
                if temp.ref == self.head:
                    temp.ref = self.head
                    return
                to_delete = temp.ref
                temp.ref = to_delete.ref
                return
            temp = temp.ref
            if temp == self.head:
                break
        print("Node not found")
    
    def delete_before_specific(self, value):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.ref == self.head:
            print("Only one node present, no node before it to delete")
            return

        temp = self.head

        # If the value is found at head, delete the last node
        if self.head.data == value:
            temp = self.head
            while temp.ref.ref != self.head:
                temp = temp.ref
            temp.ref = self.head
            return

        # Traverse to find the node before the node with `value`
        temp = self.head
        while temp.ref.ref != self.head:
            if temp.ref.ref.data == value:  # Found the node before `value`
                temp.ref = temp.ref.ref  # Bypass the node before `value`
                return
            temp = temp.ref

        print("Value not found")

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
obj1.delete_start()
obj1.print_ll()
obj1.delete_end()
obj1.print_ll()
obj1.delete_specific(40)
obj1.print_ll()
obj1.delete_after_specific(37)
obj1.print_ll()
obj1.delete_before_specific(35)
obj1.print_ll()
