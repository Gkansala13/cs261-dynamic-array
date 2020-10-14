# DynamicArray: An array that grows to accommodate new elements.
# Your implementation should pass the tests in test_dynamic_array.py.
# Grayson Kansala
import numpy as np 
class DynamicArray:

    def __init__(self):
        self.capacity=10
        self.data=np.empty(self.capacity, object )
        self.next_index=0
        
    def is_empty(self):
        if self.next_index==0:
            return True
        else: 
            return False

    def clear(self):
        self.next_index = 0
        self.data =0

    def __len__(self):
        return self.next_index
    
    def append(self, item):
        self.data[self.next_index] = item
        self.next_index+=1
        
    def __getitem__(self, index):
        if index >= self.next_index or index < 0:
            raise IndexError("Invalid index")
        return self.data[index]
    
    def pop(self):
         self.next_index -= 1
         return self.data[self.next_index]