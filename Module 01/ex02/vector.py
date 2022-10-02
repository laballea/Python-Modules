from multiprocessing.sharedctypes import Value
from typing import List


class Vector():
	def __init__(self, values):
		if (isinstance(values, int)):
			if (values > 0):
				values = [[float(i)] for i in range(values)]
			else:
				raise ValueError("Values is negative !")
		elif (isinstance(values, tuple)):
			if (not all(isinstance(item, int) for item in values)):
				raise ValueError("Tuple contains not int values !")
			if (values[1] < values[0]):
				raise ValueError("Invalid range !")
			values = [[float(i)] for i in range(values[0], values[1], 1)]
		if (not isinstance(values, list) or not all(isinstance(item, list) for item in values) ):
			raise ValueError("Values invalid format !")
		if (len(values) == 1):
			self.shape = (1, len(values[0]))
		else:
			self.shape = (len(values), 1)
		if (len(values) == 0 or not all(len(lst) != 0 for lst in values)):
			raise ValueError("Some values are empty !")
		for lst in values:
			for value in lst:
				if (not isinstance(value, float)):
					raise ValueError("Some values are not float !")
		self.values = values

	def T(self):
		if (self.shape[0] == 1):
			return Vector([[float(i)] for i in self.values[0]])
		else:
			return Vector([[float(i[0]) for i in self.values]])

	def dot(self, vector):
		if (isinstance(vector, Vector)):
			if (self.shape == vector.shape):
				if (self.shape[0] == 1):
					return sum([float(i) * float(j) for (i, j) in zip(self.values[0], vector.values[0])])
				else:
					return sum([float(i[0]) * float(j[0]) for (i, j) in zip(self.values, vector.values)])
			else:
				raise ValueError("Vectors does not have same shape !")
		raise TypeError("Can only operate vector to vector")


	def __add__(self, vector):
		if (isinstance(vector, Vector)):
			if (self.shape == vector.shape):
				if (self.shape[0] == 1):
					return Vector([[float(i) + float(j) for (i, j) in zip(self.values[0], vector.values[0])]])
				else:
					return Vector([[float(i[0]) + float(j[0])] for (i, j) in zip(self.values, vector.values)])
			else:
				raise ValueError("Vectors does not have same shape !")
		raise TypeError("Can only add vector to vector")

	def __radd__(self, vector):
		if (isinstance(vector, Vector)):
			if (self.shape == vector.shape):
				if (self.shape[0] == 1):
					return Vector([[float(i) + float(j) for (i, j) in zip(self.values[0], vector.values[0])]])
				else:
					return Vector([[float(i[0]) + float(j[0])] for (i, j) in zip(self.values, vector.values)])
			else:
				raise ValueError("Vectors does not have same shape !")
		raise TypeError("Can only operate vector to vector")

	def __sub__(self, vector):
		if (isinstance(vector, Vector)):
			if (self.shape == vector.shape):
				if (self.shape[0] == 1):
					return Vector([[float(i) - float(j) for (i, j) in zip(self.values[0], vector.values[0])]])
				else:
					return Vector([[float(i[0]) - float(j[0])] for (i, j) in zip(self.values, vector.values)])
			else:
				raise ValueError("Vectors does not have same shape !")
		raise TypeError("Can only operate vector to vector")

	def __rsub__(self, vector):
		if (isinstance(vector, Vector)):
			if (self.shape == vector.shape):
				if (self.shape[0] == 1):
					return Vector([[float(i) - float(j) for (i, j) in zip(self.values[0], vector.values[0])]])
				else:
					return Vector([[float(i[0]) - float(j[0])] for (i, j) in zip(self.values, vector.values)])
			else:
				raise ValueError("Vectors does not have same shape !")
		raise TypeError("Can only operate vector to vector")

	def __truediv__(self, scalar):
		if (isinstance(scalar, int) or isinstance(scalar, float)):
			if (scalar == 0):
				raise ZeroDivisionError()
			if (self.shape[0] == 1):
				return Vector([[float(i) / scalar for i in self.values[0]]])
			else:
				return Vector([[float(i[0]) / scalar] for i in self.values])
		elif (isinstance(scalar, Vector)):
			raise NotImplementedError("Vector division not implemented.")
		else:
			raise TypeError("Vector can only be divided by int or float.")
		# truediv : only with scalars (to perform division of Vector by a scalar).

	def __rtruediv__(self, scalar):
		raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

	def __mul__(self, scalar):
		if (isinstance(scalar, int) or isinstance(scalar, float)):
			if (self.shape[0] == 1):
				return Vector([[float(i) * scalar for i in self.values[0]]])
			else:
				return Vector([[float(i[0]) * scalar] for i in self.values])
		elif (isinstance(scalar, Vector)):
			raise NotImplementedError()
		else:
			raise TypeError("Vector can only be multiply by int or float")

	def __rmul__(self, scalar):
		if (isinstance(scalar, int) or isinstance(scalar, float)):
			if (self.shape[0] == 1):
				return Vector([[float(i) * scalar for i in self.values[0]]])
			else:
				return Vector([[float(i[0]) * scalar] for i in self.values])
		elif (isinstance(scalar, Vector)):
			raise NotImplementedError()
		else:
			raise TypeError("Vector can only be multiply by int or float")

	def __str__(self):
		return str(self.values)

	def __repr__(self):
		return str(self.values)
	
