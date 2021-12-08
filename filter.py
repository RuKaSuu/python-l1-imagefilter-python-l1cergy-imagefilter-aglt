import cv2
import numpy as np


def Dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    cv2.dilate(image, kernel, iterations=1)
    return image


def Blur(image):
    cv2.GaussianBlur(image, (59, 59), cv2.BORDER_DEFAULT)
    return image


def GrayScale(image):
    cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image



