__author__ = 'Laz.Go'

from sys import stdin
from sys import stdout
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

for inc in quicksort([int(inc) for inc in stdin.readline().split(" ")]):
    stdout.write(str(inc) + " ")