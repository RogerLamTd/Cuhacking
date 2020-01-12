#!/usr/bin/env python
# coding: utf-8

# In[66]:


import skimage
from skimage.color import rgb2gray
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import sys


# In[70]:


def grayscaleArray(filename):
    grayscale = rgb2gray(io.imread(filename))
    return grayscale


# In[67]:


def printArray(nparray):
    np.set_printoptions(threshold=sys.maxsize)
    print(nparray)


# In[ ]:





# In[ ]:




