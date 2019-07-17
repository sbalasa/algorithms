#!/bin/python3


def staircase(n):
    for i in range(n):
        print_hash = " "*(n-i-1) + "#"*(i+1)
        print(print_hash)


if __name__ == '__main__':
    n = int(input())
    staircase(n)
