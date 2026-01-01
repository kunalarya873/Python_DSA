

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

print(isPalindorome("dfndosnf"))