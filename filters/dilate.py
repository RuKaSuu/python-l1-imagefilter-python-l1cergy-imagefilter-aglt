import cv2
import numpy as np

from Logger import set_logs


def Dilate(image , kernel_size):
    """
    Apply a dilation to an image
    :param image: image to change with dilate
    :return: the image with a dilation
    """
    try:
        kernel = np.ones(kernel_size, np.uint8)
        img_dilation = cv2.dilate(image, kernel, iterations=1)
        set_logs("  Applying dilations")

        return img_dilation
    except cv2.error:
        print("Image not found")
        return None