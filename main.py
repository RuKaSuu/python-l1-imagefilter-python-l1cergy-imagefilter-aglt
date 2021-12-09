import cv2
import os
import sys
from filter import Dilate, Blur, GrayScale

args = sys.argv

liste = os.listdir('img')

for img_name in liste:
    if not img_name.endswith(('.jpg', '.png', '.jpeg')):
        print("its not a jpg or png or jpeg, it's a " + img_name)
    else:
        img_path = f'img/{img_name}'
        image = cv2.imread(img_path)
        image = GrayScale(image)
        image = Blur(image, (59,59))
        image = Dilate(image, 50)
        output = f'filtered_img/{img_name}'
        cv2.imwrite(output, image)

        print("Conversion ok " + img_name)
