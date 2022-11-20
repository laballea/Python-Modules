from ImageProcessor import ImageProcessor
imp = ImageProcessor()

imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
print(arr)
arr = imp.load("empty_file.png")
print(arr)
arr = imp.load("42AI.png")
print(arr)
imp.display(arr)
arr = imp.load("elon_canaGAN.png")
print(arr)
imp.display(arr)