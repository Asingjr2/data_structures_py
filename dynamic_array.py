"""
Implementation of pylist list which is considered a dynamic array.
Dynamix arrays increase list's byte size n batches and then create new lists with old list indices.

Example with work with python ctypes module to imitate c functionality

link to docs: https://docs.python.org/3.6/library/ctypes.html
"""
import sys
import ctypes


class DynamicArray(object):
    def __init__(self):
        self.n = 0
        self.capacity = 1   #  Used to restrict initial size
        self.A = self.make_array(self.capacity) # Used to implemnt py list

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        """Creation of index error if less than 0 index or longer than list"""
        if not 0 <= index < self.n:
            return IndexError("index not in array!!")

        return self.A[index]    # Using reference to newly sized array which copy of original

    def append(self, new_item):
        """
        Doubles maximum length of array of its full.  Updates new array with desired index and increase size count or self.n by 1.
        """
        if self.n == self.capacity:
            self._resize(2*self.capacity)   # Increasing base size of array

        self.A[self.n] = new_item
        self.n +=1

    def _resize(self, new_cap):
        """Create new array with larger capacity and then copy elements.

        new_cap = number that is 2* current capacity
        """
        B = self.make_array(new_cap)
        for item in range(self.n):
            B[item] = self.A[item]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):
        """Use ctypes library to create basic array"""
        return (new_cap * ctypes.py_object)()


# Examples creating new array and checking some functions and data
new_array = DynamicArray()
print("size of initial array is {}.".format(sys.getsizeof(new_array)))
new_array.append(1)
len(new_array)
new_array.append(800)
len(new_array)
print(new_array.capacity)
print(new_array[1])

