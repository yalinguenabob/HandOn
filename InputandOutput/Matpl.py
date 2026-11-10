import matplotlib.image as mpimg
im = mpimg.imread("../images/aa.jpg")
print(im.shape, im.dtype, im.min(), im.max())