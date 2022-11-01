import cv2
import numpy as np
img = cv2.imread('Picture1.png', cv2.IMREAD_UNCHANGED)
print(img.shape)
cv2.imshow('task', img)
cv2.waitKey()
#Extract red channel
red_channel = img[:,:,2]
#Empty image
img_red = np.zeros(img.shape)
#assign red channel to empty image
img_red[:,:,2] = red_channel
cv2.imwrite("Picture.png",img_red)
cv2.imshow("image",img_red)
cv2.waitKey()
#comment 
