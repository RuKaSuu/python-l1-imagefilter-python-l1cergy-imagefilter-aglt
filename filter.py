import cv2
import numpy as np


def Dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    img_dilation = cv2.dilate(image, kernel, iterations=1)
    cv2.imwrite('filtered_img/fond_discord.jpeg', img_dilation)


def Blur(image):
    dst = cv2.GaussianBlur(image, (59, 59), cv2.BORDER_DEFAULT)
    cv2.imwrite('filtered_img/lena.jpeg', dst)


def GrayScale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('filtered_img/lena.jpg', gray)
