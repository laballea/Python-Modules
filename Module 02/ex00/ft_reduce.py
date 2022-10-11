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
    try:
        value = iterable[0]
        for el in iterable[1:]:
            value = function_to_apply(value, el)
        return value
    except Exception:
        return None


# initializing list
lis = [1, 3, 5, 6, 2, ]

# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(reduce(operator.add, lis))
print(ft_reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(reduce(operator.mul, lis))
print(ft_reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(reduce(operator.add, ["geeks", "for", "geeks"]))
print(ft_reduce(operator.add, ["geeks", "for", "geeks"]))
