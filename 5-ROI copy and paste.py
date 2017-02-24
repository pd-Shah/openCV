

import numpy as np
import cv2
from matplotlib import  pyplot as plt

img= cv2.imread("1.jpg")
ROI= img[0:500,200:500]
img[0:500,0:300]=ROI
plt.imshow(img)
plt.imsave("this",img)
plt.show()
