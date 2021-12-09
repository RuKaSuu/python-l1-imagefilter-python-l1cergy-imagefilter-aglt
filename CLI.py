import cv2
import os
import sys

import filter
from filter import Dilate, Blur, GrayScale

args = sys.argv
argument = {}


def Start():
    liste = os.listdir('img')

    for img_name in liste:

        if not img_name.endswith(('.jpg', '.png', '.jpeg')):
            print("its not a jpg or png or jpeg, it's a " + img_name)
        else:
            img_path = f'{inputdir}/{img_name}'
            image = cv2.imread(img_path)
            if 'blur' in argument:
                print("blur")
                image = Blur(image, (argument["blur"], argument["blur"]))
                print("blur ok")

            if 'dilate' in argument:
                print("dilate")
                image = Dilate(image, (argument["dilate"]))
                print("dilate ok")

            if 'grayscale' in argument:
                print("grayscale")
                image = GrayScale(image)
                print("grayscale ok")

            output = f'{outputdir}/{img_name}'
            cv2.imwrite(output, image)

            print("Conversion ok " + img_name)
            # print('filtered_img/' + i)


# résultat cli dictionnaire


for i, a in enumerate(args):

    if a == "--input-dir":
        inputdir = args[i + 1]
        print(inputdir)

    elif a == "--output-dir":
        outputdir = args[i + 1]
        print(outputdir)

    elif a == "--filter":
        params = args[i + 1].split("|")


        for param in params:
            param = param.split(":")

            if param[0] == "grayscale":
                argument[param[0]] = 0
            else:
                argument[param[0]] = int(param[1])



    elif a == "--start":
        Start()
