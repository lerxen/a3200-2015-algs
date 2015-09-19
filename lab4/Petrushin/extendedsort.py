__author__ = "Dmitry Petrushin"

from sys import stdin
from sys import stdout


def merge(li1, li2):
    a = 0
    b = 0
    length = len(li1) + len(li2)
    res = [0 for i in range(0, length)]
    for i in range(0, length):
        if b < len(li2) and a < len(li1):
            if li1[a] > li2[b]:
                res[i] = li2[b]
                b += 1
            else:
                res[i] = li1[a]
                a += 1
        elif b < len(li2):
            res[i] = li2[b]
            b += 1
        else:
            res[i] = li1[a]
            a += 1
    return res


def mergesort(li):
    length = len(li)
    n = 1
    while n < length:
        shift = 0
        while shift < length:
            if shift + n >= length:
                break
            if shift + n * 2 > length:
                two_size = length - (shift + n)
            else:
                two_size = n
            arr2 = merge(li[shift:shift + n], li[shift + n:shift + n + two_size])
            for i in range(0, n + two_size):
                li[shift + i] = arr2[i]
            shift += n * 2
        n *= 2
    return li


def insertionsort(li):
    for i in range(1, len(li)):
        j = i
        while j > 0 and li[j - 1] > li[j]:
            li[j - 1], li[j] = li[j], li[j - 1]
            j -= 1
    return li


def extendedsort(li):
    if len(li) < 100:
        return insertionsort(li)
    else:
        return merge(extendedsort(li[0:len(li) // 2]), extendedsort(li[len(li) // 2 + 1:len(li)]))


lis = [int(n) for n in stdin.readline().split(" ")]
for i in extendedsort(lis):
    stdout.write(str(i) + " ")
