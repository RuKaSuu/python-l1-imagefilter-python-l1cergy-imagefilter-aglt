import cv2
import numpy as np

from Logger import set_logs


def Dilate(image):
    try:
        kernel = np.ones((5, 5), np.uint8)
        img_dilation = cv2.dilate(image, kernel, iterations=1)
        set_logs("  Applying dilations")

        return img_dilation

    except cv2.error:
        print("Image not found")
        return None


def Blur(image):
    try:
        dst = cv2.GaussianBlur(image, (59, 59), cv2.BORDER_DEFAULT)
        set_logs("  Applying Blur")

        return dst
    except cv2.error:
        print("Image not found")
        return None


def GrayScale(image):
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        set_logs("  Applying grayscale")

        return gray
    except cv2.error:
        print("Image not found")
        return None
