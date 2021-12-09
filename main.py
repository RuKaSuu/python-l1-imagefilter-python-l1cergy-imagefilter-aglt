import cv2
import os
import sys

args = sys.argv

from filter import Dilate, Blur, GrayScale

liste = os.listdir('img')

# Dilate(cv2.imread('img/fondDiscord.jpeg'))
# cv2.imwrite('filtered_img/fondDiscord.jpeg')

# for i in range(0 , len(args)):
#     arg = args[i]
#     print(arg)
#     if arg == '--filters':


for img_name in liste:

    if not img_name.endswith('.jpeg' or '.png' or '.jpg'):
        print("its  ot a jpg or png or jpeg, it's a " + img_name)
    else:
        img_path = f'img/{img_name}'
        image = cv2.imread(img_path)
        image = GrayScale(image)
        image = Blur(image)
        image = Dilate(image)

        output = f'filtered_img/{img_name}'
        cv2.imwrite(output, image)

        print("Conversion ok " + img_name)
        # print('filtered_img/' + i)
