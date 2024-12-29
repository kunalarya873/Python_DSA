#Queue implementation using list

queue = []

queue.insert(0, 1) #insert at the beginning of the list
queue.insert(0, 2)
queue.insert(0, 3)
queue.insert(0, 4)

# print("Queue after inserting")
# print(queue)
# print(queue.pop()) #pop the last element 4
# print(queue.pop()) #pop the last element 3
# print(queue.pop()) #pop the last element 2
# print(queue.pop()) #pop the last element 1



from collections import deque

queue = deque()
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)
queue.appendleft(4)
# print(queue) #deque([4, 3, 2, 1])
# print(queue.pop()) #pop the last element 1
# print(queue.pop()) #pop the last element 2
# print(queue.pop()) #pop the last element 3
# print(queue.pop()) #pop the last element 4


#Queue implementation using collections.deque

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
# print(queue) #deque([1, 2, 3, 4])
# print(queue.popleft()) #pop the first element 1
# print(queue.popleft()) #pop the first element 2
# print(queue.popleft()) #pop the first element 3
# print(queue.popleft()) #pop the first element 4


# Priority Queue implementation using list
q = []

q.append(1565)
q.append(22422)
q.append(3234)
q.append(444)


q.sort(reverse=True)
# print(q.pop(0)) #pop the highest priority element 22422



#Queue implementation using queue module

import queue
q = queue.PriorityQueue()

q.put(10)
q.put(1)
q.put(5)
q.put(3)

# print(q.get()) #pop the highest priority element 10



#Circular Queue implementation

class CircluarQ:
    def __init__(self, n):
        self.n = n
        self.array = [None] * n
        self.front = 0
        self.rear = 0
        self.size = 0

    def equeue(self, data):
        if self.size >= self.n:
            raise Exception("Queue is full")
        self.array[self.rear] = data
        self.rear = (self.rear + 1) % self.n
        self.size += 1
        return self

    def dequeue(self):
        if self.size == 0:
            raise Exception("Queue is empty, Underflow condition")
        temp = self.array[self.front]
        self.array[self.front] = None
        self.front = (self.front + 1) % self.n
        self.size -= 1
        return temp
    
    def display(self):
        print(self.array)
        print("Front:", self.front)
        print("Rear:", self.rear)
        print("Size:", self.size)
        return self
    
q = CircluarQ(5)
q.equeue(1).display()
# [1, None, None, None, None]
# Front: 0
# Rear: 1
# Size: 1
q.equeue(2).display()
# [1, 2, None, None, None]
# Front: 0
# Rear: 2
# Size: 2
q.equeue(3).display()
# [1, 2, 3, None, None]
# Front: 0
# Rear: 3
# Size: 3
print(q.dequeue())
# 1
q.equeue(4).display()
# [None, 2, 3, 4, None]
# Front: 1
# Rear: 4
# Size: 3
q.equeue(5).display()
# [None, 2, 3, 4, 5]
# Front: 1
# Rear: 0
# Size: 4
print(q.dequeue())
# 2
q.equeue(6).display()
# [6, None, 3, 4, 5]
# Front: 2
# Rear: 1
# Size: 4
q.equeue(7).display()
# [6, 7, 3, 4, 5]
# Front: 2
# Rear: 2
# Size: 5
print(q.dequeue())
# 3
q.equeue(8).display()
# [6, 7, 8, 4, 5]
# Front: 3
# Rear: 3
# Size: 5


# 1




# 3
