# Stack implementation using list
stack = []

stack.append('a')
stack.append('b')
stack.append('c')
# print("stack is ",stack)  # ['a', 'b', 'c']


# print("pop from stack is ",stack.pop())  # c
# print("stack is ",stack)  # ['a', 'b']
# print("pop from stack is ",stack.pop())  # b
# print("stack is ",stack)  # ['a']
# print("pop from stack is ",stack.pop())  # a
# print("stack is ",stack)  # []



# Stack implementation using deque
from collections import deque

stack = deque(maxlen=3)
stack.append('a')
stack.append('b')
stack.append('c')
print("stack is ",stack)  # ['a', 'b', 'c']
print("pop from stack is ",stack.pop())  # c
print("stack is ",stack)  # ['a', 'b']
print("pop from stack is ",stack.pop())  # b
print("stack is ",stack)  # ['a']
print("pop from stack is ",stack.pop())  # a
print("stack is ",stack)  # []
print("pop from stack is ",stack.pop())  # IndexError: pop from an empty deque


# Stack implementation using queue
from queue import LifoQueue
stack = LifoQueue(maxsize=3)
stack.put('a')
stack.put('b')
stack.put('c')
print("stack is ",stack.queue)  # ['a', 'b', 'c']
print("pop from stack is ",stack.get())  # c
print("stack is ",stack.queue)  # ['a', 'b']
print("pop from stack is ",stack.get())  # b
print("stack is ",stack.queue)  # ['a']
print("pop from stack is ",stack.get())  # a
print("stack is ",stack.queue)  # []
print("pop from stack is ",stack.get())  # IndexError: pop from an empty deque