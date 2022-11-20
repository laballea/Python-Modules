import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from ColorFilter import ColorFilter
from ColorFilter import ImageProcessor

imp = ImageProcessor()
clrFilter = ColorFilter()
arr = imp.load("elon_canaGAN.png")

imp.display(clrFilter.invert(arr))
imp.display(clrFilter.to_blue(arr))
imp.display(clrFilter.to_green(arr))
imp.display(clrFilter.to_red(arr))
imp.display(clrFilter.to_celluloid(arr))
imp.display(clrFilter.to_grayscale(arr, "m"))
imp.display(clrFilter.to_grayscale(arr, "w", weights=[0.2, 0.3, 0.5]))