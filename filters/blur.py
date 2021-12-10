import cv2

from Logger import set_logs


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
