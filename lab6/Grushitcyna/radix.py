from sys import stdin
import math


elem = [int(s) for s in stdin.readline().split()]


def i_digit(n, i):
    d = n % (10 ** (i + 1)) / (10 ** i)
    return d


def h_m_digits(n):
    t = int(math.log10(n) + 1)
    return t


def k_max(elem):
    max = elem[0]
    for i in range(1, len(elem)):
        if max < elem[i]:
            max = elem[i]
    return max


def counting_sort(elem, f):
    final = [0 for x in range(len(elem))]
    order = [0 for x in range(10)]
    for j in range(len(elem)):
        order[i_digit(elem[j], f)] += 1
    for i in range(1, 10):
        order[i] += order[i - 1]
    j = len(elem) - 1
    while j >= 0:
        order[i_digit(elem[j], f)] -= 1
        final[order[i_digit(elem[j], f)]] = elem[j]
        j -= 1
    return final


def radix_sort(elem):
    n = h_m_digits(k_max(elem))
    for i in range(0, n):
        elem = counting_sort(elem, i)
    return elem


print(radix_sort(elem))
