import math
from math import factorial

testlist = [5, 4, 7, 8, 9, 1, 2, 6, 3]

def merge(list, begin, mid, legth):
    return


def mergesort(list, begin, length):
    if begin < length:
        mid = math.floor((begin+length)/2)
        mergesort(list, begin, mid)
        mergesort(list, mid + 1, begin)
        merge(list, begin, mid, length)
    return list

mergesort(list, 0, len(testlist) - 1)
print(testlist)

"""
[5, 4, 7, 8, 9, 1, 2, 6, 3, 0]
[5, 4, 7, 8, 9| 1, 2, 6, 3, 0]
[5, 4| 7, 8, 9| 1, 2| 6, 3, 0]
[5| 4| 7| 8, 9| 1| 2| 6| 3, 0]
[5| 4| 7| 8| 9| 1| 2| 6| 3| 0]
"""
