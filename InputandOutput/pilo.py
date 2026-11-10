from PIL import Image
import numpy as np
#im = Image.open("../images/photo.jpg") #Load image
#print(im.width,im.height,im.mode,im.format,im.size,type(im), im.info)
#im.show(im)
with open("../images/photo.jpg", "rb") as f:
    im = Image.open(f); im.show()
im_gray = im.convert('L') #convert RGB image to  grayscale
im_gray.save("../images/Photo_gray.jpg") #save to disk
print(im_gray.size)
# 3840, 2160 (w,h)
print(np.array(im_gray).shape)
#(h,w)