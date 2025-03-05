class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None

    def add_starting(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            tail = self.head.prev  # Find the last node
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def print(self):
        if self.head is None:
            print("CDLL is empty")
        else:
            temp = self.head
            while True:
                print(temp.data, "<=>", end=" ")
                temp = temp.next
                if temp == self.head:
                    print()
                    break

    def add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            tail = self.head.prev  # Get the last node
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
    
    def delete_starting(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return

        tail = self.head.prev
        self.head = self.head.next
        self.head.prev = tail 
        tail.next = self.head  
    
    def delete_ending(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        if self.head.next == self.head:
            self.head = None
            return

        tail = self.head.prev
        tail.prev.next = self.head
        self.head.prev = tail.prev

        # Optional: Cleanup memory reference
        tail.next = None
        tail.prev = None
        tail = None


# Testing the corrected implementation
obj1 = Circular_Doubly_Linked_List()
obj1.add_starting(10)
obj1.add_ending(20)
obj1.add_ending(30)
obj1.add_starting(5)
obj1.delete_starting()
obj1.delete_ending()
obj1.print()
