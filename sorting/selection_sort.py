"""
@uthor: Abdullahi S. Adamu
"""
import array
from absl import logging
from datetime import datetime
from queue import PriorityQueue

logging.set_verbosity(logging.DEBUG)

def sort_by_selection_sort(arr):
    """ 
    Sorting using a Priority Queue

    Python uses a heap for priority queues so this is likely a heap sort
    
    """
    start = datetime.now()
    # array of integers
    _arr = array.array('i', arr)
    # nummber of elements
    n = len(_arr)

    for i in range(0, n):
        # set element zero as current min
        curr_min_index = i
        # find min from i+1 ...n
        for j in range(i +1 , n):
            if (_arr[j] < _arr[curr_min_index]):
                curr_min_index = j
        # if not same as initial min, swap
        if curr_min_index != i:
            _arr[i],_arr[curr_min_index] = _arr[curr_min_index],_arr[i]
    
    time_taken = datetime.now() - start

    return {'result': _arr, 'time_taken': time_taken}




