from sys import stdin
import random

def quicksort(arr):
    left = []
    med = []
    right = []

    if len(arr) > 1:
        r = random.randint(0,len(arr) - 1)
        pt = arr[r]
        for x in arr:
            if x < pt:
                left.append(x)
            if x == pt:
                med.append(x)
            if x > pt:
                right.append(x)
        left = quicksort(left)
        right = quicksort(right)
        ans = left + med + right
        return ans    
    else:
        return arr

arr = [int(n) for n in stdin.readline().split(" ")]
random.seed()
print(quicksort(arr))
