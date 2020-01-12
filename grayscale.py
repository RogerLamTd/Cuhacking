
import skimage
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import sys


grayscale = rgb2gray(skimage.io.imread("./chicken.jpg"))


fig, ax = plt.subplots(figsize=(4,8))
ax.imshow(grayscale, cmap=plt.cm.gray)
ax.set_title("Grayscale")
plt.show()



#np.set_printoptions(threshold=sys.maxsize)
#print(grayscale)



