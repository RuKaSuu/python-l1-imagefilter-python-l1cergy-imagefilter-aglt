import cv2
import numpy as np


def Dilate(image , kernel_size):
    try:
        kernel = np.ones(kernel_size, np.uint8)
        img_dilation = cv2.dilate(image, kernel, iterations=1)
        return img_dilation
    except cv2.error:
        print("Image not found")
        return None


def Blur(image , blur_size):
    try:
        dst = cv2.GaussianBlur(image, blur_size, cv2.BORDER_DEFAULT)
        return dst
    except cv2.error:
        print("Image not found")
        return None


def GrayScale(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray
    except cv2.error:
        print("Image not found")
        return None
