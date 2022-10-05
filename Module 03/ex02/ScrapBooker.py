import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

class ImageProcessor():
	def load(self, path):
		"""
			opens the PNG file specified by the path argument and returns an
			array with the RGB values of the pixels image. It must display a message specifying
			the dimensions of the image (e.g. 340 x 500).
		"""
		try:
			img = Image.open(path)
			print("Image dimensions: {}.".format(img.size))
			return np.asarray(img, dtype=np.uint8)
		except Exception as inst:
			print(inst)
			return None

	def display(self, array):
		"""
			takes a numpy array as an argument and displays the corre-
			sponding RGB image
		"""
		plt.imshow(array, interpolation='nearest')
		plt.show()

class ScrapBooker():
	def crop(self, array, dim, position=(0,0)):
		"""
		Crops the image as a rectangle via dim arguments (being the new height
		and width of the image) from the coordinates given by position arguments.
		Args:
		-----
		array: numpy.ndarray
		dim: tuple of 2 integers.
		position: tuple of 2 integers.
		Return:
		-------
		new_arr: the cropped numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if (not (isinstance(dim, tuple) and list(map(type, dim)) == [int, int] and len(dim) == 2)):
			print("Invalid dimensions type !")
			return None
		if (not (isinstance(position, tuple) and list(map(type, position)) == [int, int] and len(position) == 2)):
			print("Invalid position type !")
			return None
		if (not isinstance(array, np.ndarray)):
			print("Invalid array type !")
			return None
		if (position[0] + dim[0] + 1 > array.shape[0] or position[1] + dim[1] > array.shape[1]):
			print("Combinaison of parameters not compatible !")
			return None
		return array[position[0]:dim[0] + 1,position[1]:dim[1]]

	def thin(self, array, n, axis):
		"""
		Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
		Args:
		-----
		array: numpy.ndarray.
		n: non null positive integer lower than the number of row/column of the array
		(depending of axis value).
		axis: positive non null integer.
		Return:
		-------
		new_arr: thined numpy.ndarray.
		None (if combinaison of parameters not compatible).
		Raise:
		------
		This function should not raise any Exception.
		"""
		if (not isinstance(array, np.ndarray)):
			print("Invalid array type !")
			return None
		if (not (isinstance(axis, int) and (axis == 0 or axis == 1))):
			print("Invalid axis type !")
			return None
		if (axis == 1):
			axis = 0
			max = array.shape[0]
		else:
			axis = 1
			max = array.shape[1]
		if (not (isinstance(n, int) and n >= 0 and n <= max)):
			print("Invalid n type !")
			return None
		return np.delete(array, [x - 1 for x in range(n, max + 1, n)], axis=axis)
	def juxtapose(self, array, n, axis):
		"""
		Juxtaposes n copies of the image along the specified axis.
		Args:
		-----
		array: numpy.ndarray.
		n: positive non null integer.
		axis: integer of value 0 or 1.
		Return:
		-------
		new_arr: juxtaposed numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if (not isinstance(array, np.ndarray)):
			print("Invalid array type !")
			return None
		if (not (isinstance(axis, int) and (axis == 0 or axis == 1))):
			print("Invalid axis type !")
			return None
		if (not isinstance(n, int)):
			print("Invalid n type !")
			return None
		return np.concatenate([array] * n, axis=axis)

	def mosaic(self, array, dim):
		"""
		Makes a grid with multiple copies of the array. The dim argument specifies
		the number of repetition along each dimensions.
		Args:
		-----
		array: numpy.ndarray.
		dim: tuple of 2 integers.
		Return:
		-------
		new_arr: mosaic numpy.ndarray.
		None (combinaison of parameters not compatible).
		Raises:
		-------
		This function should not raise any Exception.
		"""
		if (not isinstance(array, np.ndarray)):
			print("Invalid array type !")
			return None
		if (not (isinstance(dim, tuple) and list(map(type, dim)) == [int, int] and len(dim) == 2)):
			print("Invalid dim type !")
			return None
		array = np.concatenate([array] * dim[0], axis=0)
		return np.concatenate([array] * dim[1], axis=1)

spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
print(spb.crop(arr1, (1,3),(1,0)))
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print(spb.thin(arr2, 3, 0))
arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))

imp = ImageProcessor()
arr = imp.load("42AI.png")
imp.display(spb.crop(arr, (100,100),(0,0)))
imp.display(spb.thin(arr, 3, 0))
imp.display(spb.juxtapose(arr, 3, 1))
imp.display(spb.mosaic(arr, (3, 3)))