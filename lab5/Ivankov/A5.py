__author__ = 'Laz.Go'

from sys import stdin
import random

def quicksort(array):
    if len(array) < 2:
        return array

    rand = random.Random()
    key = array[rand.randrange(0, len(array))]
    left = []
    middle = []
    right = []
    for i in range(0, len(array)):
        if array[i] == key:
            middle.append(array[i])
        elif array[i] < key:
            left.append(array[i])
        elif array[i] > key:
            right.append(array[i])
    return quicksort(left) + middle + quicksort(right)

array = [int(s) for s in stdin.readline().split()]
array = quicksort(array)
print(array)