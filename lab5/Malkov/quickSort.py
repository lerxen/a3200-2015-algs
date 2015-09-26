from sys import stdin, stdout
import random

def quick_sort(start, end):
    if start < end:
        middle = partition(start, end)
        quick_sort(start, middle - 1)
        quick_sort(middle + 1, end)

def partition(start, end):
    pivot = arr[random.randint(0, len(arr) - 1)]
    pivot, arr[end] = arr[end], pivot
    i = start - 1
    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

arr = [int(i) for i in stdin.readline().split()]
quick_sort(0, len(arr) - 1)
stdout.write(" ".join(map(str, arr)))
