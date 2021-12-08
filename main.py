import cv2
import numpy as np

img = cv2.imread('img/fond_discord.jpeg')

kernel = np.ones((5, 5), np.uint8)
image = cv2.imread('img/lena.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

src = cv2.imread('img/lena.jpeg', cv2.IMREAD_UNCHANGED)
dst = cv2.GaussianBlur(src, (59, 59), cv2.BORDER_DEFAULT)


img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imwrite('filtered_img/fond_discord.jpeg', img_dilation)
cv2.imwrite('filtered_img/lena.jpg', gray)
cv2.imwrite('filtered_img/lena.jpeg', dst)

cv2.waitKey(0)




