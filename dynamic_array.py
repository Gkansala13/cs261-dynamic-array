# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# YOUR NAME

import numpy as np 
class DynamicArray:

    def __init__(self):
        self.capacity=10
        

    def is_empty(self):
        return True

    def __len__(self):
        return 0