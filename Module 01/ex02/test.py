from decimal import DivisionByZero
from vector import Vector
import unittest

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class TestVector(unittest.TestCase):
	def test_init(self):
		with self.assertRaises(ValueError):
			Vector("not list") # not a list
		with self.assertRaises(ValueError):
			Vector([["lol"]])
		with self.assertRaises(ValueError):
			Vector([[]])
		with self.assertRaises(ValueError):
			Vector([])
		with self.assertRaises(ValueError):
			Vector(-5)
		with self.assertRaises(ValueError):
			Vector((2, 1))
		Vector([[5.], [8.], [9.], [10.]])
		Vector([[5., 8., 9., 10.]])
		print(bcolors.OKGREEN + "INIT TEST SUCCESS" + bcolors.ENDC)
	def test_mult(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		v2 = v1 * 5
		self.assertEqual(v2.values, [[0.0], [5.0], [10.0], [15.0]])

		v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
		v2 = v1 * 5
		self.assertEqual(v2.values, [[0.0, 5.0, 10.0, 15.0]])

		with self.assertRaises(NotImplementedError):
			v1 * v2
		with self.assertRaises(TypeError):
			v1 * "lol"
	
	def test_div(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		v2 = v1 * 5
		v2 = v2 / 5
		self.assertEqual(v2.values, v1.values)

		with self.assertRaises(ZeroDivisionError):
			v2 = v1 / 0
		with self.assertRaises(NotImplementedError):
			v1 / v2
		with self.assertRaises(TypeError):
			v1 / "lol"
		with self.assertRaises(NotImplementedError):
			5 / v1

	def test_add(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		v2 = Vector([[1.0], [2.0], [3.0], [4.0]])
		v2 = v1 + v2
		self.assertEqual(v2.values, [[1.0], [3.0], [5.0], [7.0]])

		v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
		v2 = Vector([[1.0, 2.0, 3.0, 4.0]])
		v2 = v1 + v2
		self.assertEqual(v2.values, [[1.0, 3.0, 5.0, 7.0]])
		
		with self.assertRaises(ValueError):
			v2 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0]])
			v1 = v1 + v2
		with self.assertRaises(TypeError):
			v1 = v1 + 5

	def test_sub(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		v2 = Vector([[1.0], [2.0], [3.0], [4.0]])
		v2 = v1 - v2
		self.assertEqual(v2.values, [[-1.0], [-1.0], [-1.0], [-1.0]])

		v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
		v2 = Vector([[1.0, 2.0, 3.0, 4.0]])
		v2 = v1 - v2
		self.assertEqual(v2.values, [[-1.0, -1.0, -1.0, -1.0]])
		
		with self.assertRaises(ValueError):
			v2 = Vector([[1.0, 2.0, 3.0, 4.0, 5.0]])
			v1 = v1 - v2
		with self.assertRaises(TypeError):
			v1 = v1 - 5
	
	def test_T(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		self.assertEqual(v1.T().values, [[0.0, 1.0, 2.0, 3.0]])

		v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
		self.assertEqual(v1.T().values, [[0.0], [1.0], [2.0], [3.0]])

	def test_dot(self):
		v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
		v2 = Vector([[1.0], [2.0], [3.0], [4.0]])
		self.assertEqual(v1.dot(v2), 20)


def main():
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape) # Expected output (4,1)
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).values) # Expected output [[0.0], [1.0], [2.0], [3.0]]
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape) # Expected output (1,4)
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).values) # Expected output [[0.0, 1.0, 2.0, 3.0]]
	print(Vector(5).values) # Expected output [[0.0, 1.0, 2.0, 3.0]]
	print(Vector((5, 10)).values) # Expected output [[0.0, 1.0, 2.0, 3.0]]

	print(Vector([[0.0, 1.0, 2.0, 3.0]]).dot(Vector([[1.0, 2.0, 3.0, 4.0]])))
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).dot(Vector([[1.0], [2.0], [3.0], [4.0]])))
	print(Vector([[0.0, 1.0, 2.0, 3.0]]).T())
	print(Vector([[0.0], [1.0], [2.0], [3.0]]).T())

if __name__ == '__main__':
	main()
	print()
	print("UNITTEST")
	print()

	unittest.main()
