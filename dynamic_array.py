# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Grayson Kansala
import numpy as np 
class DynamicArray:

    def __init__(self):
        self.capacity=10
        self.data=np.empty(self.capacity, object )
        self.size=0
        
    def is_empty(self):
        return True

    def __len__(self):
        return 0
    
    def append(self, item):
        self.data[self.size] = item
      
        
    def __getitem__(self, index):
        return self.data[index]
    