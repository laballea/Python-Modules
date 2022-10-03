from typing import Iterable


def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if (not isinstance(iterable, Iterable)):
		raise TypeError("{} is not iterable".format(type(iterable).__name__))
	try:
		for el in iterable:
			if (function_to_apply(el)):
				yield el
	except:
		return None

numbers = [10, 15, 21, 33, 42, 55]
print(filter(lambda dum: not (dum % 2), numbers))
print(ft_filter(lambda dum: not (dum % 2), numbers))