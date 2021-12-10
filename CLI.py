import cv2
import os
import sys
from art import tprint
from Logger import set_logs
import  configparser

from filter import Dilate, Blur, GrayScale, FilterZeTeam

configuration = configparser.ConfigParser()
args = sys.argv
argument = {
    'inputdir' : '',
    'outputdir' : '',
    'filter' : '',
}

def MainController():

    def Start():
        """
        Start the program
        :return: the image with the filter applied
        """
        liste = os.listdir('img')

        for img_name in liste:

            if not img_name.endswith(('.jpg', '.png', '.jpeg')):
                set_logs("  Its not a jpg or png or jpeg, it's a " + img_name)
            else:

                img_path = f'{inputdir}/{img_name}'
                image = cv2.imread(img_path)
                if 'blur' in argument:
                    set_logs("  blur")
                    image = Blur(image, (argument["blur"], argument["blur"]))
                    set_logs("  blur ok")

                if 'dilate' in argument:
                    set_logs("  dilate")
                    image = Dilate(image, (argument["dilate"]))
                    set_logs("  dilate ok")

                if 'grayscale' in argument:
                    set_logs("  grayscale")
                    image = GrayScale(image)
                    set_logs("  grayscale ok")

                if 'FilterZeTeam' in argument:
                    set_logs("  FilterZeTeam")
                    image = FilterZeTeam(image)
                    set_logs("  FilterZeTeam ok")


                output = f'{outputdir}/{img_name}'
                cv2.imwrite(output, image)

                set_logs("  Conversion ok " + img_name)
                # print('filtered_img/' + i)


    # résultat cli dictionnaire


    for i, a in enumerate(args):

        if a == "--input-dir":
            inputdir = args[i + 1]
            print(inputdir)

        elif a == "--output-dir":
            outputdir = args[i + 1]
            print(outputdir)

        elif "--help" == a:
            set_logs("  Help menu activated")

            tprint("HELP => ")

            # Afficher les commandes qu'on peut utiliser et pourquoi faire
            print("💡 | --filter / --f  => Appliquer des filtres aux photos du dossier")
            print("💡 | --input  / --i  => Mettre le nom du dossier à importer")
            print("💡 | --output / --o  => Mettre le nom du dossier où les images seront envoyées")

        elif "--config-files" == a:
            config = args[i + 1]
            configuration.read(config)

            inputdir = configuration['DEFAULT']['imputdir']
            outputdir = configuration['DEFAULT']['outputdir']
            argument['filter']= configuration['FILTERS']['filters']
            split = argument['filter'].split('|')
            for split2 in split:
                split2= split2.split(':')
                print(split2)




        elif a == "--filter":
            params = args[i + 1].split("|")


            for param in params:
                param = param.split(":")

                if param[0] == "grayscale":
                    argument[param[0]] = 0
                elif param[0] == "FilterZeTeam":
                    argument[param[0]] = 0
                else:
                    argument[param[0]] = int(param[1])


    Start()
