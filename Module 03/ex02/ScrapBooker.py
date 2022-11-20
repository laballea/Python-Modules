import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


class ImageProcessor():
    def __init__(self):
        print("ImageProcessor init")

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
    def __init__(self):
        print("Scrap init")

    def crop(self, array, dim, position=(0, 0)):
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
        try:
            if (not (isinstance(dim, tuple) and list(map(type, dim)) == [int, int] and len(dim) == 2)):
                return None
            if (not (isinstance(position, tuple) and list(map(type, position)) == [int, int] and len(position) == 2)):
                return None
            if (not isinstance(array, np.ndarray)):
                return None
            if (position[0] + dim[0] + 1 > array.shape[0] or position[1] + dim[1] > array.shape[1]):
                return None
            return array[position[0]:dim[0] + 1, position[1]:dim[1]]
        except Exception:
            return None

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
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            if (not (isinstance(axis, int) or not (axis == 0 or axis == 1))):
                return None
            if (axis == 1):
                axis = 0
                max = array.shape[0]
            else:
                axis = 1
                max = array.shape[1]
            if (not (isinstance(n, int) and n >= 0 and n <= max)):
                return None
            return np.delete(array, [x - 1 for x in range(n, max + 1, n)], axis=axis)
        except Exception:
            return None

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
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            if (not (isinstance(axis, int) or not (axis == 0 or axis == 1))):
                return None
            if (not isinstance(n, int) or n <= 0):
                return None
            return np.concatenate([array] * n, axis=axis)
        except Exception:
            return None

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
        try:

            if (not isinstance(array, np.ndarray)):
                return None
            if (not (isinstance(dim, tuple) and list(map(type, dim)) == [int, int] and len(dim) == 2)):
                return None
            array = np.concatenate([array] * dim[0], axis=0)
            return np.concatenate([array] * dim[1], axis=1)
        except Exception:
            return None
