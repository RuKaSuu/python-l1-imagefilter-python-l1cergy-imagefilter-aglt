import cv2
import os
from filter import Dilate, Blur, GrayScale


liste = os.listdir('img')


#Dilate(cv2.imread('img/fond_discord.jpeg'))
#cv2.imwrite('filtered_img/fond_discord.jpeg')

for img_name in liste:
    img_path = f'img/{img_name}'
    image = cv2.imread(img_path)
    image = GrayScale(image)
    # image = Blur(image)
    # image = Dilate(image)

    output = f'filtered_img/{img_name}'
    cv2.imwrite(output, image)

    print(img_path)
    print(image)
    #print('filtered_img/' + i)


