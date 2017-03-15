from math import log
from random import shuffle
from time import time

def merge(begin, middle, end, A, temp):
    pos1 = begin
    pos2 = middle
    pos3 = begin
    while pos1 < middle and pos2 < end:
        if A[pos1] < A[pos2]:
            temp[pos3] = A[pos1]
            pos1 += 1
            pos3 += 1
        else:
            temp[pos3] = A[pos2]
            pos2 += 1
            pos3 += 1
    if pos1 == middle:
        temp[pos3:end] = A[pos2:end]
    else:
        temp[pos3:end] = A[pos1:end]
    A[begin:end] = temp[begin:end]

def merge_sort_r(begin, end, A, temp):
    if end - begin > 1:
        middle = (begin + end) / 2
        merge_sort_r(begin, middle, A, temp)
        merge_sort_r(middle, end, A, temp)
        merge(begin, middle, end, A, temp)

def merge_sort(A):
    n = len(A)
    temp = [0] * n
    merge_sort_r(0, n, A, temp)
    return A

def test(N):
    l = [1000, 5000, 10000, 50000, 100000, 500000]
    for n in l:
        A = range(n)
        shuffle(A)
        start_time = time()
        print range(n) == merge_sort(A)
        print (time() - start_time)/(n * n)

test(6)



        
        
