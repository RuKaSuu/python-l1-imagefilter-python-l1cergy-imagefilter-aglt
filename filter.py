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


def Blur(image , blur_size):
    """
        Apply a blur to an image
        :param image: image to change with blur
        :return: the image with a blur
        """

    if (blur_size[0] % 2) == 0 and (blur_size[1] % 2) == 0:
        try:
            blur = cv2.blur(image, blur_size)
            set_logs("  Applying Blur")
            return blur
        except cv2.error:
            print("Image not found")
            return None
    else:

        try:
            dst = cv2.GaussianBlur(image, blur_size, cv2.BORDER_DEFAULT)
            return dst
        except cv2.error:
            print("Image not found")
            return None





def GrayScale(image):
    """
        Apply a grayscale to an image
        :param image: image to change with grayscale
        :return: the image with a grayscale
        """
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        set_logs("  Applying grayscale")

        return gray
    except cv2.error:
        print("Image not found")
        return None


def FilterZeTeam(image):
    filter =cv2.putText(image, "#AGLT_CORP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    return filter