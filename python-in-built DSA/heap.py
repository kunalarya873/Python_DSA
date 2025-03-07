def buildheap(arr):
    non_leaf_node = len(arr)//2 -1
    for i in range(non_leaf_node, -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    largest = i
    left_child = 2*i+1
    right_child = 2*i+2

    if left_child < len(arr) and arr[left_child] > arr[largest]:
        largest = left_child
    
    if right_child < len(arr) and arr[right_child] > arr[largest]:
        largest = right_child
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def printheap(arr):
    print("Array Representation of heap is")

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

import math
from io import StringIO
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        output.write(str(n).center(col_width, fill))
        last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return
if __name__ == "__main__":
    arr = [2, 4, 5, 6,7,8, 12, 33, 454,565, 222, 899, 90, 33]
    buildheap(arr)
    printheap(arr)
    show_tree(arr)