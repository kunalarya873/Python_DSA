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
        new_node.ref = self.head
        temp = self.head
        while(temp.ref != self.head):
            temp = temp.ref
        temp.ref = new_node
        self.head = new_node