from sorting.insertion_sort import sort_by_insertion_sort
from array import array
from absl import logging

logging.set_verbosity(logging.DEBUG)



def test_empty():
    # test array
    arr = array('i', [])
    # get result
    result = sort_by_insertion_sort(arr)['result']
    # assertion
    assert arr == result

    
def test_sorted():
    # test array
    arr = array('i', list(range(1, 100)))
    logging.debug(f'array: {arr}')
    # get result
    result = sort_by_insertion_sort(arr)['result']
    logging.debug(f'result: {result}')
    # sort
    assert arr == result


def test_unsorted_signed():
    # test array
    arr = array('i', [0, 2,1,3, -1])
    logging.debug(f'array: {arr}')
    # get result
    result = sort_by_insertion_sort(arr)['result']
    logging.debug(f'result: {result}')
    # sort
    assert array('i', [-1, 0, 1, 2, 3]) == result


def test_unsorted_unsigned():
    # test array
    arr = array('i', [0, 2, 3, 6, 7, 9, 1])
    logging.debug(f'array: {arr}')
    # get result
    result = sort_by_insertion_sort(arr)['result']
    logging.debug(f'result: {result}')
    # assertion
    assert array('i', [0, 1, 2, 3, 6, 7, 9]) == result


def test_unsorted_with_dupplicates():
    # test array
    arr = array('i', [0, 1, 10, 304, 99, 1, 9, 10, 2])
    logging.debug(f'array: {arr}')
    # get result
    result = sort_by_insertion_sort(arr)['result']
    logging.debug(f'result: {result}')
    # assertion
    assert array('i', [0, 1, 1, 2, 9, 10, 10, 99, 304]) == result









