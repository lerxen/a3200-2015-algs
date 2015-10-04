from sys import stdin
import sys


elements = [int(s) for s in stdin.readline().split()]


def insertion_sort(arr):
    for j in xrange(1, len(arr)):
        i = j - 1
        while (i >= 0) and (arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            i -= 1


def merge(arr, left, middle, right):
    n1 = middle - left
    n2 = right - middle
    l_part = [arr[left + i] for i in range(n1)]
    r_part = [arr[middle + i] for i in range(n2)]
    l_part.append(2**64)
    r_part.append(2**64)
    i = 0
    j = 0
    for k in range(left, right):
        if l_part[i] <= r_part[j]:
            arr[k] = l_part[i]
            i += 1
        else:
            arr[k] = r_part[j]
            j += 1


def merge_sort(arr, left, right, pointer):
    if right - left <= pointer:
        insertion_sort(arr)
    else:
        middle = (left + right) // 2
        merge_sort(arr, left, middle, pointer)
        merge_sort(arr, middle, right, pointer)
        merge(arr, left, middle, right)


merge_sort(elements, 0, len(elements) - 1, 10)
for i in elements:
    sys.stdout.write(str(i) + ' ')
