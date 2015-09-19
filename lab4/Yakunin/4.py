from sys import stdin

def insertSort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
    return arr

def merge(left,right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    while len(left) > 0:
        result.append(left[0])
        left.pop(0)
    while len(right) > 0:
        result.append(right[0])
        right.pop(0)
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        left = []
        right = []
        middle = int(len(arr) / 2)
        for i in range(middle):
            left.append(arr[i])
        for i in range(middle, len(arr)):
            right.append(arr[i])
        if len(left) > 100:
            left = mergeSort(left)
        else:
            left = insertSort(left)
        if len(right) > 100:
            right = mergeSort(right)
        else:
            right = insertSort(right)
        return merge(left, right)

arr = [int(n) for n in stdin.readline().split(" ")]
print(mergeSort(arr))
