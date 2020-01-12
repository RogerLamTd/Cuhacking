#!/usr/bin/env python
# coding: utf-8

# In[66]:


import skimage
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import sys


# In[70]:


def grayscaleArray(filename):
    grayscale = rgb2gray(skimage.io.imread(filename))
    fig, ax = plt.subplots(figsize=(4,8))
    ax.imshow(grayscale, cmap=plt.cm.gray)
    ax.set_title("Grayscale")
    plt.show()
    return grayscale


# In[67]:


def printArray(nparray):
    np.set_printoptions(threshold=sys.maxsize)
    print(nparray)


# In[ ]:





# In[ ]:




