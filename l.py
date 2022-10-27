import cv2
import numpy as np

img = cv2.imread('Picture1.png', cv2.IMREAD_UNCHANGED)
print(img.shape)
cv2.imshow('sec', img)
cv2.waitKey()
red_channel = img[:,:,2]
img_red = np.zeros(img.shape)
img_red[:, :, 2] = red_channel
cv2.imwrite("R.png", img_red)
cv2.imshow("photo", img_red)
cv2.waitKey()