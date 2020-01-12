#!/usr/bin/env python
# coding: utf-8

# In[66]:


import skimage
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
import sys


# In[63]:


grayscale = rgb2gray(skimage.io.imread("./chicken.jpg"))


fig, ax = plt.subplots(figsize=(4,8))
ax.imshow(grayscale, cmap=plt.cm.gray)
ax.set_title("Grayscale")
plt.show()


# In[67]:


np.set_printoptions(threshold=sys.maxsize)
print(grayscale)


# In[ ]:





# In[ ]:




