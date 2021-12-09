import sys
from art import tprint
from Logger import set_logs

from art import tprint

from Logger import set_logs

args = sys.argv

for i, a in enumerate(args):
    #print(a)
    #print(args)
    if "--input-dir" == a:
        print("input : ")
        inputdir = args[i + 1]
        print(inputdir)

    elif "--output-dir" == a:
        print("output : ")
        outputdir = args[i + 1]
        print(outputdir)

    elif "--filter" == a or "--f" == a:
        print("filtre")
        #prendre la valeur des filtres de la case d'après

    elif "--help" == a:
        set_logs("  Help menu activated")

        tprint("HELP => ")

        #Afficher les commandes qu'on peut utiliser et pourquoi faire
        print("💡 | --filter / --f  => Appliquer des filtres aux photos du dossier")
        print("💡 | --input  / --i  => Mettre le nom du dossier à importer")
        print("💡 | --output / --o  => Mettre le nom du dossier où les images seront envoyées")

    elif "--list--filters" == a:
        set_logs("  Help menu activated")

        tprint("HELP => ")

        #Afficher les commandes qu'on peut utiliser et pourquoi faire
        print("💡 | --filter / --f  => Appliquer des filtres aux photos du dossier")
        print("💡 | --input  / --i  => Mettre le nom du dossier à importer")
        print("💡 | --output / --o  => Mettre le nom du dossier où les images seront envoyées")

    elif "--filter" == a or "--f" == a:
        print("filtre")
        #prendre la valeur des filtres de la case d'après

    elif "--help" == a:
        set_logs("Help menu activated")

        tprint("HELP => ")

        #Afficher les commandes qu'on peut utiliser et pourquoi faire
        print("💡 | --filter / --f  => Appliquer des filtres aux photos du dossier")
        print("💡 | --input  / --i  => Mettre le nom du dossier à importer")
        print("💡 | --output / --o  => Mettre le nom du dossier où les images seront envoyées")




#résultat cli dictionnaire