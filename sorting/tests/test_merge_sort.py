"""
Tests for Insertion Sort

@author: Abdullahi S. Adamu
"""

from sorting.merge_sort import merge_sort
from array import array
from absl import logging

logging.set_verbosity(logging.DEBUG)



def test_empty():
    # test array
    arr = array('i', [])
    _arr = array('i', arr)
    # get result
    merge_sort(_arr)
    # assertion
    assert arr == _arr


def test_sorted():
    # test array
    arr = array('i', list(range(1, 100)))
    _arr = array('i', arr)
    logging.debug(f'array: {arr}')
    # get result
    merge_sort(_arr)
    logging.debug(f'result: {_arr}')
    # sort
    assert arr == _arr


def test_unsorted_signed():
    # test array
    arr = array('i', [0, 2,1,3, -1])
    _arr = array('i', arr)
    logging.debug(f'array: {arr}')
    # get result
    merge_sort(_arr)
    logging.debug(f'result: {_arr}')
    # sort
    assert array('i', [-1, 0, 1, 2, 3]) == _arr


def test_unsorted_unsigned():
    # test array
    arr = array('i', [0, 2, 3, 6, 7, 9, 1])
    _arr = array('i', arr)
    logging.debug(f'array: {arr}')
    # get result
    merge_sort(_arr)
    logging.debug(f'result: {_arr}')
    # assertion
    assert array('i', [0, 1, 2, 3, 6, 7, 9]) == _arr


def test_unsorted_with_dupplicates():
    # test array
    arr = array('i', [0, 1, 10, 304, 99, 1, 9, 10, 2])
    _arr = array('i', arr)
    logging.debug(f'array: {arr}')
    # get result
    merge_sort(_arr)
    logging.debug(f'result: {_arr}')
    # assertion
    assert array('i', [0, 1, 1, 2, 9, 10, 10, 99, 304]) == _arr









