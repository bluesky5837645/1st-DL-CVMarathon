import  cv2
import numpy as np

img=cv2.imread('lena.png',cv2.IMREAD_COLOR)
print(img.shape)
print(img.shape[0])