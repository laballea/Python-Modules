from functools import reduce
from typing import Iterable
import operator


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """
    if (not isinstance(iterable, Iterable)):
        raise TypeError("{} is not iterable".format(type(iterable).__name__))
    if (function_to_apply == None):
        raise TypeError("{} is not iterable".format(type(iterable).__name__))
    try:
        value = iterable[0]
        for el in iterable[1:]:
            value = function_to_apply(value, el)
        return value
    except Exception:
        return None
