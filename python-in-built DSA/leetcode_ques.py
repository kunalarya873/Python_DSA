

# Day 1
def armstrongNumber(num: int)-> bool:
    total = 0
    nod = list(str(num))

    while num> 0:
        last_digit = num%10
        total += last_digit*len(nod)
        num=num//10
    return num == total

# print(armstrongNumber(153))
# print(armstrongNumber(128))


import math
# Print all factors of a given number
def giveFactors(num: int):
    factors = set()
    factors.add(1)
    i = 2
    while i<math.sqrt(num)+1:
        if num%i == 0:
            factors.add(i)
            factors.add(num//i)
        i+=1
    factors.add(num)
    return factors

# print(giveFactors(10))
# print(giveFactors(36))
# print(giveFactors(8888))



# Frequency in a dictionary

def addFrequency(nums):
    frequency_map = dict()
    for i in nums:
        if i in frequency_map:
            frequency_map[i]+=1
        else:
            frequency_map[i]=1

    hashmap = dict()
    for i in nums:
        hashmap[i] = hashmap.get(i, 0) + 1

    return frequency_map

# print(addFrequency([1,3,4,5,22,55,1, 2,3, 4,5, 22, 1, 1]))



def hashingNumber(n, m):
    hashmap_n = dict()
    for i in n:
        hashmap_n[i] = hashmap_n.get(i, 0) + 1
    res = dict()
    for i in m:
        if i in hashmap_n:
            res[i] = hashmap_n[i]
    return res

# print(hashingNumber("wfdzfndsfnsdfndsfbsdfsoiqjeroiqehfn",["w", 'f', "n", "d"]))


def sumOfN(n):
    if n == 1:
        return 1

    return n+sumOfN(n-1)

def factorial(n):
    if n == 1:
        return 1
    return n+factorial(n-1)

def reverseOfArray(arr, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    if start >= end:
        return arr

    arr[start], arr[end] = arr[end], arr[start]
    return reverseOfArray(arr, start + 1, end - 1)

# print(reverseOfArray([11, 2, 3, 4, 5, 6, 7]))


def isPalindorome(string) -> bool:
    curr = list(str(string))
    reverse = curr[::-1]

    return curr == reverse

# print(isPalindorome("dfndosnf"))


def selectionSort(arr: list)-> list:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] <arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def selectionSortIncr(arr: list)-> list:
    for i in range(len(arr)):
        max_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr


# print(selectionSortIncr([3, 5,63, 6, 2, 6, 11, 6, 1, 3,5,6,]))

def bubbleSort(arr: list)-> list:
    for i in range(len(arr)-2, -1, -1):
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

# print(bubbleSort([3, 5,63, 6, 2, 6, 11, 6, 1, 3,5,6,]))

def insertionSort(arr:list)->list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j]<key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

# print(insertionSort([3, 5,63, 6, 2, 6, 11, 6, 1, 3,5,6,]))



def mergeSortedArray(arr1, arr2):
    result = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    while i<n and j<m:
        if arr1[i]< arr2[j]:
            result.append(arr1[i])
            i+=1
        else:
            result.append(arr2[j])
            j+=1
    if i < n:
        while i<n:
            result.append(arr1[i])
            i+=1
    if j<m:
        while j<m:
            result.append(arr2[j])
            j+=1
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)

    return mergeSortedArray(left_arr, right_arr)

# print(mergeSort([3, 5,63, 6, 2, 6, 11, 6, 1, 3,5,6,]))



#Largest array in matrix

arr = [1,3 -44,65,-644, 223, -44354, -632, -123,5,-4545,1,2345, -24, -55, 523,33,-534]

def findLargestNumArray(arr):
    least = arr[0]
    for i in arr:
        if i > least:
            least = i
    return least

def findSecondLargest(arr: list):
    sec_larg = float("-inf")
    for i in range(len(arr)):
        if arr[i] > sec_larg and arr[i] !=  max(arr):
            sec_larg = arr[i]
    return sec_larg

print(mergeSort(arr))
print(findSecondLargest(arr))