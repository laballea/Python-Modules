# function prototype
import random
import string


def generator(text:str, sep=" ", option=None):
	"""
		Splits the text according to sep value and yield the substrings.
		option precise if a action is performed to the substrings before it is yielded.
	"""

	if (not isinstance(text, str) or not all(c in string.printable for c in text)):
		yield "ERROR"
		return
	if (not isinstance(sep, str)):
		yield "ERROR"
		return
	if (option not in [None, "shuffle", "unique", "ordered"]):
		yield "ERROR"
		return

	result = text.split(sep)
	if (option == "ordered"):
		result.sort()
	elif (option == "unique"):
		result = list(dict.fromkeys(result))
	elif (option == "shuffle"):
		random.shuffle(result)

	for i in result:
		yield i