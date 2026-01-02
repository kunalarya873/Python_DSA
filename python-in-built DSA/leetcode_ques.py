

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

# print(mergeSort(arr))
# print(findSecondLargest(arr))

def isArrayReversed(arr: list) -> bool:
    return arr == arr[::-1]

def isArraySorted(arr:list) -> bool:
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            return False
    return True

# print(isArraySorted([1, 2, 3, 4, 5, 6]))

def removeDuplicates(arr:list)-> list:
    new_arr = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        new_arr.append(arr[i])
    new_arr.append(arr[-1])
    return new_arr

# print(removeDuplicates([1, 2,2, 3, 3,3, 4, 4, 4, 5, 6, 6, 6, 7]))
from typing import List

def maxRotateFunction(nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        total_sum = sum(nums)
        current_value = sum(i * nums[i] for i in range(len(nums)))
        max_value = current_value

        for i in range(1, len(nums)):
            current_value += total_sum - len(nums) * nums[-i]
            max_value = max(max_value, current_value)
        return max_value


def moveZeroes(nums: List[int]) -> None:
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return
    
nums = [0,1,0,3,12]
# moveZeroes(nums)
# print(nums)


def mergeSortedArray(arr1: list, arr2: list):
    sortedArray = []
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0

    while i < n and j <m:
        if arr1[i] <= arr2[j]:
            if len(sortedArray) == 0 or sortedArray[-1] != arr1[i] :
                sortedArray.append(arr1[i])
            i+=1
        else:
            if len(sortedArray) == 0 or sortedArray[-1] != arr2[j]:
                sortedArray.append(arr2[j])
            j+=1
    while i < n:
        if len(sortedArray) == 0 or sortedArray[-1] != arr1[i]:
            sortedArray.append(arr1[i])
        i+=1

    while j < m:
        if len(sortedArray) == 0 or sortedArray[-1] != arr2[j]:
            sortedArray.append(arr2[j])
        j+=1

    return sortedArray


# print(mergeSortedArray([1, 2, 3, 4, 5, 5, 5, 6, 6], [1,2,2, 3,3,3, 4, 4, 5, 5, 6 ,8, 9]))


def missingNumber(nums: List[int]) -> int:
    arr = [i for i in range(len(nums)+1)]
    for i in arr:
        if i in nums:
            continue
        else:
            return i
    return -1

# print(missingNumber([3,0,1]))

import collections

def repeatedNTimes(nums: List[int]) -> int:
        frequency = collections.defaultdict()
        for i in nums:
            frequency[i] = frequency.get(i, 0)+1
        highFrequency = max(frequency.values())
        for key, val in frequency.items():
            if val == highFrequency:
                return key


def findMaxConsecutiveOnes(nums: List[int]) -> int:
        cons = 0
        res =0
        for i in nums:
            if i == 1:
                cons +=1
                res = max(cons, res)
            else:
                cons = 0
        return res


def lengthOfLastWord( s: str) -> int:
        list_of_str = list(s)
        len_of_list_str = len(list_of_str)
        last_word = []

        for i in range(1, len_of_list_str):
            if list_of_str[-i] == " ":
                continue
            elif list_of_str[-i] != " " and list_of_str[-i-1] == " ":
                break
            else:
                last_word.append(list_of_str[-i])
        return len(last_word) +1

# print(lengthOfLastWord("   fly me   to   the moon  "))

# print(repeatedNTimes([2,1,2,5,3,2]))


def maxSubArrya(arr:list)->int:
    
    i, j = 0, 1
    maxi = float("-inf")
    total = 0
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            maxi = max(total, maxi)

    return maxi


def maxArray(arr:list)->int:
    high = float("-inf")
    total = 0
    for i in arr:
        total += i
        high = max(total, high)
        if total<0:
            total =0
    return high

# print(maxArray([5,4,-1,7,8]))


def maxProfit(arr: list)-> int:
    profit = 0
    min_price = float("inf")
    for i in range(len(arr)):
        min_price = min(arr[i], min_price)
        profit = max(profit, arr[i]-min_price)

    return profit


# print(maxProfit([7,1,5,3,6,4]))

def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    longest = 0
    count = 0
    last_smaller = float("-inf")
    for i in range(len(nums)):
        num = nums[i]
        if num -1 == last_smaller:
            count +=1
            last_smaller = num
        elif num != last_smaller:
            count =1
            last_smaller =  num
        longest = max(count, longest)
    return longest

print(longestConsecutive([7,1,5,3,6,4]))
