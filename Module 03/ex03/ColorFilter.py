import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)


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
            img = Image.open(path).convert('RGB')
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
        plt.imshow(array.astype(np.uint8), interpolation='nearest')
        plt.show()


class ColorFilter():
    def __init__(self):
        print("ColorFilter init")

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            im_IVT = 255 - array.copy()
            return im_IVT
        except:
            return None

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            im_B = array.copy()
            im_B[:, :, (0, 1)] = 0
            return im_B
        except:
            return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            im_G = array.copy()
            im_G[:, :, (0, 2)] = 0
            return im_G
        except:
            return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            im_R = array.copy()
            im_R[:, :, (1, 2)] = 0
            return im_R
        except:
            return None

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not isinstance(array, np.ndarray)):
                return None
            im_cel = array.copy()
            n_shade = 10
            for x in range(0, n_shade):
                shade = array[:, :, :] > (x) * 255 / n_shade
                im_cel[shade] = (x + 1) * 255 / n_shade
            return im_cel
        except:
            return None

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = "mean"/"m": performs the mean of RBG channels.
        For filter = "weight"/"w": performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ["m","mean","w","weight"]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        try:
            if (not (isinstance(filter, str) and filter in ["m", "mean", "w", "weight"])):
                return None
            if (not isinstance(array, np.ndarray)):
                return None
            if (filter in ["w", "weight"] and not (kwargs["weights"] and
                isinstance(kwargs["weights"], list) and
                list(map(type, kwargs["weights"])) == [float, float, float] and sum(kwargs["weights"]) == 1)):
                return None
            im_gray = array.copy()
            if (filter in ["m", "mean"]):
                im_gray[:] = np.sum(im_gray, axis=-1, keepdims=1)/3
            else:
                im_gray[:] = np.sum(im_gray, axis=-1, keepdims=1)/3
                im_gray = im_gray[:, :, :] * kwargs["weights"]

            return im_gray
        except:
            return None
