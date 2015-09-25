from sys import stdin
import random

def quickSort(arr):
    less = []
    equal = []
    more = []
    if len(arr) < 2:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    for i in range(len(arr)):
        if arr[i] < pivot:
            less.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            more.append(arr[i])
    return quickSort(less) + equal + quickSort(more)

arr = [int(i) for i in stdin.readline().split()]
arr = quickSort(arr)
print(arr)
