"""
Merge Sort implementation 

@author: Abdullahi S. Adamu
"""
import os
from absl import logging
from array import array
from typing import List
from datetime import datetime

DEBUG = os.environ.get('DEBUG', False)

if DEBUG:
    logging.set_verbosity(logging.DEBUG)


def merge(arr_a, arr_b, s_arr):
    """
    merges two arrays by copying elements from both arrays 

    params:
        arr_a = sub array A of length n
        arr_b = sub array B of length m
        s_arr = sub array S of length n + m
    """
    i = 0
    j = 0
    # len of sub_array
    n = len(arr_a) 
    m = len(arr_b) 
    n_s = n + m
    while (i + j < n_s):
        j_elapsed = j == m
        i_elapsed = i == n
        if (j_elapsed) or (not i_elapsed and arr_a[i] <= arr_b[j]):
            s_arr[i + j] = arr_a[i]
            i +=1
        elif (i_elapsed) or (not j_elapsed and arr_b[j] <= arr_a[i]):
            s_arr[i + j] = arr_b[j]
            j +=1

def merge_sort(arr):
    """
    Runs merge sort on an array 

    Recursively splits into smaller sub-arrays (split)
    and the merged subarrays back in ascending order (merge)

    params:
        arr - List[int] array of integers
    
    returns 
        arr - array of sorted integer values

    """
    # lenght of list
    n = len(arr)

    if n < 2:
        # base case - already sorted
        return 

    # find midpoint
    mid = n//2
    # divide
    arr_a = array('i', arr[0 : mid])
    arr_b = array('i', arr[mid: n])
    # print split
    logging.debug(f'splitting into: {arr_a} and {arr_b}')
    
    # pass on for further splits
    merge_sort(arr_a)
    merge_sort(arr_b)

    # recursively merge back
    logging.debug(f'merging into {arr_a} and {arr_b}')
    merge(arr_a, arr_b, arr)
