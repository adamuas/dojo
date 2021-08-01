"""
@uthor: Abdullahi S. Adamu
"""
import array
from absl import logging
from datetime import datetime

logging.set_verbosity(logging.DEBUG)

def sort_by_insertion_sort(arr):
    start = datetime.now()
    # array of integers
    _arr = array.array('b', arr)

    n  = len(arr)
    for k in range(1, n):
        logging.debug(f'k: {k}')
        # store current elemenet
        curr = _arr[k]
        logging.debug(f'curr: {curr}')
        # store current 
        j = k
        while (j > 0 and _arr[j - 1] > curr):
            # shift backward
            _arr[j] = _arr[j -1]
            # decreament j
            j -=1
        
        _arr[j] = curr
    
    time_taken = datetime.now() - start
    
    return {'result': _arr, 'time_taken': _arr}




