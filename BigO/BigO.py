def multiply(n):
    return n*n # O(1) complexity
print(multiply(9))

def print_items(n):
    for i in range(n):
        print(i)#O(n) time Complexity
print_items(10)

def print_item(n):
    for i in range(n):
        for j in range(i):
            print(i, j) # 0(n^2) time Complexity Because of Nested Loop

def printItem(n):
    for i in range(n):
        for j in range(j):
            for k in range(j):
                print(i, j, k) # O(n^3) time complexity 
def dropNonDominantOperation(n):
    for i in range(n):
        for j in range(i):
            print(i, j)
    for k in range(n):
        print(k)
        # O(n^2+n) is equal to O(n^2)

def sum1(n):
    if n<=0: #Space Complexity
        return 0
    return n + sum1(n-1)
print(sum1(3))

def pair_sum_sequence(n):#Space Complexity
    total = 0
    for i in range(n):
        total = total + pair_sum(i, i+1)
    return total
def pair_sum(a, b):
    return a+b

def findBiggestNumber(sampleArray):
    biggestNum= sampleArray[0]
    for index in range(1, len(sampleArray)):
        if sampleArray[index] > biggestNum:
            biggestNum = sampleArray[index]
        print(biggestNum)