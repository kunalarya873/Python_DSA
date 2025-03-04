class Node:
    def __init__(self, data):
        self.pref = None
        self.nref = None
        self.data = data

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_starting(self, data):
        if self.head is None:
            pass