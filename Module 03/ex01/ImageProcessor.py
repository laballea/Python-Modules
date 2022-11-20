from array import array
import sys
from PIL import Image
import numpy
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
            return numpy.asarray(img, dtype=numpy.uint8)
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
