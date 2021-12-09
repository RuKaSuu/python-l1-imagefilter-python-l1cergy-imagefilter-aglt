import cv2
import os
from Logger import set_logs
from filter import Dilate, Blur, GrayScale

#args = sys.argv

liste = os.listdir('img')


for img_name in liste:

    if not img_name.endswith(('.jpeg', '.png', '.jpg')):
        print("its  ot a jpg or png or jpeg, it's a " + img_name)
    else:
        img_path = f'img/{img_name}'
        image = cv2.imread(img_path)
        image = GrayScale(image)
        image = Blur(image)
        image = Dilate(image)
        image = cv2.putText(image, "#AGLT_CORP", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        set_logs("  Conversion images")

        output = f'filtered_img/{img_name}'
        cv2.imwrite(output, image)

        print("\n Conversion ok " + img_name + '\n')
