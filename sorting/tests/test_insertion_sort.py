from sorting.insertion_sort import sort_by_insertion_sort
from array import array
from absl import logging

logging.set_verbosity(logging.DEBUG)

def test_sorted():
    # test array
    arr = array('b', list(range(1, 100)))
    logging.debug(f'array: {arr}')
    # sort
    assert arr == sort_by_insertion_sort(arr)['result'] 


def test_unsorted_unsigned():
    # test array
    arr = array('b', [0, 2,1,3, -1])
    logging.debug(f'array: {arr}')
    # sort
    assert array('b', [-1, 0, 1, 2, 3]) == sort_by_insertion_sort(arr)['result'] 


     



