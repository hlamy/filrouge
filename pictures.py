# coding=UTF-8
# importation de fonctions de la librairie "pillow" pour assurer la manipulation des images
from PIL import Image as img
from PIL.ExifTags import TAGS
# utilisation de la librairie 'Path' pour assurer une bonne gestion des chemins de fichiers
from pathlib import Path
# importation de fonctions de la librairie "os" pour gérer la recherche dans les fichiers
from os import walk, remove
from os.path import isfile, join
# importation de json pour générer les fichiers de métadonnées
import json
from random import randint


# fonction d'ouverture et d'extraction des métadonnées d'une image:
def extractMetadata(picturepath, metadata):
    if True:
        with img.open(picturepath) as pic:

            # On récupere certaines données spécifique de l'image grâce aux méthodes de la librairie 'pillow':
            metadata['picture_Format'] = pic.format
            metadata['picture_Size'] = pic.size
            metadata['picture_Mode'] = pic.mode

            # Avec la librairie ExifTags de pillow, on peut récurérer les métadonnées de type EXIF (métadonnées de photographie) :
            try:
                metadata['picture_EXIF'] = True
                for tag, valeur in pic._getexif().items():
                    if tag in TAGS:
                        if str(TAGS[tag])!='MakerNote':
                            metadata['picture_exif_' + str(TAGS[tag])] = convertvalue(valeur)

            except AttributeError:
                # Une métadonnée pour signifier que les métadonnées de type photographique EXIF n'ont pu être récupérées
                metadata['picture_EXIF'] = False

    # En cas d'erreur en entrée/sortie (impossible d'ouvrir l'image), le système retourne une erreur dans le dictionnaire de métadonnée :
    # except IOError:
    #     pass

    return metadata

# fonction de convertion, dans le format qui semble le plus approprié (pour réinjection dans le JSON contenant les métadonnées) :
def convertvalue(value):
    # entiers, décimaux et chaînes de caractères sont possibles. 
    # Retourne None s'il n'est pas possible de convertir en "string" :
    possibleFormats = [int, float, str]
    for f in possibleFormats:
        try:
            return f(value)
        except:
            pass
    return None



