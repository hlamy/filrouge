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
# importation d'éléments fourni par AWS pour l'utilisation du service Rekognition
from rekognition_objects import RekognitionText
import boto3

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

    try:
        metadata['picture_textFoundByAwsRekognition'] = str(trouve_text(picturepath))
    except:
        metadata['picture_textFoundByAwsRekognition'] = 'No texte could be retrieved from picture'
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

# Classe de détection de texte dans une image, construite a partir de code récupéré sur les tutoriels AWS
class RekognitionImage:
    """
    Encapsulates an Amazon Rekognition image. This class is a thin wrapper
    around parts of the Boto3 Amazon Rekognition API.
    """
    def __init__(self, image, image_name, rekognition_client):
        """
        Initializes the image object.

        :param image: Data that defines the image, either the image bytes or
                      an Amazon S3 bucket and object key.
        :param image_name: The name of the image.
        :param rekognition_client: A Boto3 Rekognition client.
        """
        self.image = image
        self.image_name = image_name
        self.rekognition_client = rekognition_client
    
    @classmethod
    def from_file(cls, image_file_name, rekognition_client, image_name=None):
        """
        Creates a RekognitionImage object from a local file.

        :param image_file_name: The file name of the image. The file is opened and its
                                bytes are read.
        :param rekognition_client: A Boto3 Rekognition client.
        :param image_name: The name of the image. If this is not specified, the
                           file name is used as the image name.
        :return: The RekognitionImage object, initialized with image bytes from the
                 file.
        """
        with open(image_file_name, 'rb') as img_file:
            image = {'Bytes': img_file.read()}
        name = image_file_name if image_name is None else image_name
        return cls(image, name, rekognition_client)

    def detect_text(self):
        """
        Detects text in the image.
        :return The list of text elements found in the image.
        """
        if True:
        # try:
            response = self.rekognition_client.detect_text(Image=self.image)
            texts = [RekognitionText(text) for text in response['TextDetections']]
            return texts
        # except:
            print('pb')
        # else:
            # return texts

# fonction de recherche de texte
def trouve_text(filepath):
    rekognition_client = boto3.client('rekognition')
    text_string = ''
    imageCherchable = RekognitionImage.from_file(Path(filepath), rekognition_client)
    textes = imageCherchable.detect_text()
    print(textes)
    for i in range(len(textes)):
        text_string += ' ' + str(textes[i].to_dict()['text'])


    return  text_string

if __name__ == '__main__':
    print(trouve_text("./trashcan/texte.jpg"))