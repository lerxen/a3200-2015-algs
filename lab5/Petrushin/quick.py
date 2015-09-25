__author__ = 'Dmitry Petrushin'

from sys import stdin
from sys import stdout
import random


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    rand = random.Random()
    pivot = arr[rand.randrange(0, len(arr))]
    lt = []
    gt = []
    eq = []
    for i in range(0, len(arr)):
        if arr[i] == pivot:
            eq.append(arr[i])
        elif arr[i] < pivot:
            lt.append(arr[i])
        elif arr[i] > pivot:
            gt.append(arr[i])
    return quicksort(lt) + eq + quicksort(gt)


for elem in quicksort([int(elem) for elem in stdin.readline().split(" ")]):
    stdout.write(str(elem) + " ")
