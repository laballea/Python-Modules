from typing import Iterable
import numpy


class NumPyCreator():
    def __init__(self):
        print("NumpyCreator init")

    def from_list(self, lst, dtype=None):
        """
            takes a list or nested lists and returns its corresponding Numpy array
        """
        try:
            if (not isinstance(lst, list)):
                return None
            it = iter(lst)
            the_len = len(next(it))
            if not all(len(el) == the_len for el in it):
                return None
            return numpy.array(lst, dtype=dtype)
        except Exception:
            return None

    def from_tuple(self, tpl, dtype=None):
        """
            takes a tuple or nested tuples and returns its corresponding Numpy array
        """
        try:
            if (not isinstance(tpl, tuple) or any(isinstance(item, tuple) for item in tpl)):
                return None
            return numpy.array(tpl, dtype=dtype)
        except Exception:
            return None

    def from_iterable(self, itr, dtype=None):
        """
            takes a iterable and returns its corresponding Numpy array
        """
        try:
            if (not isinstance(itr, Iterable)):
                return None
            return numpy.fromiter(itr, dtype=dtype)
        except Exception:
            return None

    def from_shape(self, shape, value=0, dtype=None):
        """
            returns an array filled with the same value.
            The first argument is a tuple which specifies the shape of the array, and the second
            argument specifies the value of the element
        """
        try:
            return numpy.full(shape, value, dtype)
        except Exception:
            return None

    def random(self, shape, dtype=None):
        """
            returns an array filled with random values. It takes as an
            argument a tuple which specifies the shape of the array.
        """
        try:
            return numpy.random.randn(shape[0], shape[1]).astype(dtype)
        except Exception:
            return None

    def identity(self, n, dtype=None):
        """
            returns an array representing the identity matrix of size n.
        """
        try:
            return numpy.identity(n, dtype)
        except Exception:
            return None
