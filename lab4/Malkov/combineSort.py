from sys import stdin, stdout

def countMin(n):
    flag = 0
    while n >= 64:
        flag += n & 1
        n >>= 1
    return n + flag

def insertionSort(arr):
    for i in range(0, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            x = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = x
            j -= 1
    return arr
            
def combineSort(arr):
    if len(arr) < minrun:
        arr = insertionSort(arr)
    else:
        arr[0:int(n / 2)] = combineSort(arr[0:int(n / 2)])
        arr[int(n / 2):n] = combineSort(arr[int(n / 2):n])
    return arr

def merge(arr, left, mid, right):
    it1 = 0
    it2 = 0
    result = [0] * (right - left)
  
    while left + it1 < mid and mid + it2 < right:
        if arr[left + it1] < arr[mid + it2]:
            result[it1 + it2] = arr[left + it1]
            it1 += 1
        else:
            result[it1 + it2] = arr[mid + it2]
            it2 += 1
  
    while left + it1 < mid:
        result[it1 + it2] = arr[left + it1]
        it1 += 1
  
    while mid + it2 < right:
        result[it1 + it2] = arr[mid + it2]
        it2 += 1
  
    for i in range(0, it1 + it2):
        arr[left + i] = result[i]
    
    return result
        
arr = [int(elem) for elem in stdin.readline().split(' ')]
n = len(arr)
minrun = countMin(n)
arr = combineSort(arr)
arr = merge(arr, 0, int(n / 2), n)
print(arr)
