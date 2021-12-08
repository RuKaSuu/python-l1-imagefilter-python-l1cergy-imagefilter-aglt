import cv2
import os
import numpy as np
from filter import Dilate, Blur, GrayScale

liste = os.listdir('img')


Dilate(cv2.imread('img/fond_discord.jpeg'))
cv2.imwrite('filtered_img/fond_discord.jpeg')


for i in liste:
    GrayScale(cv2.imread(i))


    print('filtered_' + i)


