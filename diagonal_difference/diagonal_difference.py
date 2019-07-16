#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    new_arr = [j for i in arr for j in i]
    ld = 0
    rd = 0
    length = len(arr[0])

    def generate_ld(length):
        limit = length+1
        i = 0
        count = 1
        while count <= length:
            yield i
            i += limit
            count += 1

    def generate_rd(length):
        limit = length-1
        i = limit
        count = 1
        while count <= length:
            yield i
            i += limit
            count += 1
    l_value = generate_ld(length)
    r_value = generate_rd(length)
    for _ in arr:
        ld += new_arr[l_value.__next__()]
        rd += new_arr[r_value.__next__()]
    return abs(ld - rd)


if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
