import cv2

from Logger import set_logs


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
