from typing import Iterable


def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    if (not isinstance(iterable, Iterable)):
        raise TypeError("{} is not iterable".format(type(iterable).__name__))
    if (function_to_apply == None):
        raise TypeError("{} is not iterable".format(type(iterable).__name__))

    try:
        for el in iterable:
            yield function_to_apply(el)
    except Exception:
        return None
