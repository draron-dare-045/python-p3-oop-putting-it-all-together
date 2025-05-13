#!/usr/bin/env python3

class Shoe:
    #initialization takes place here
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
    # returns a function to an attribute
    @property
    def size(self):
        return self._size
    # Checking whether input fits required status
    @size.setter
    def size(self,value):
        if isinstance (value, int) :
            self._size = value
        else:
            print("size must be an integer")
    # a new function that prints when it is called
    def cobble(self):
        print("Your shoe is as good as new!")
        # instance attribute
        self.condition = "New" 
    