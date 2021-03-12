# utilities
# coding=UTF-8
# importation de datetime pour obtenir les informations sur l'heure
from datetime import date, datetime
import json
from pathlib import Path
# si besoin de crypto : importation fernet
# from cryptography.fernet import Fernet
import os
from os import walk, remove
import base64
from filetype import guess
import magic
import boto3
import pictures


temporary_files_folder = './temp'
# code de création d'ajout dans le fichier json du fichier encodé en base64

def code64fichier(filepath):
    with open(filepath, 'rb') as fichier:
        encodedfile = base64.b64encode(fichier.read())
    return str(encodedfile)


def extractgenericmetadata(datafile, metadatafile, filepath, original_filepath):
    # création du chemin du fichier (lorsque stocké dans le dossier temporaire)
    # filepath = temporary_files_folder / Path(datafile['given_name'])

    # donne la taille du fichier
    try:
        size = os.path.getsize(filepath)
    except:
        size = None 
    metadatafile['size'] = size


    # donne le nom et l'extension du fichier tels qu'envoyés
    try:
        nomfichier, extensionfichier = os.path.splitext(original_filepath)
    except:
        nomfichier = None
        extensionfichier = None

    # ajoute le nom et l'extension dans le dictionnaire
    try:
        metadatafile['given_extension'] = extensionfichier
    except:
        pass
    # donne la date de derniere modification du fichier
    try:
        time = os.path.getmtime(filepath) 
    except:
        time = None
    
    metadatafile['datemodified'] = str(datetime.fromtimestamp(time))

    # donne le type du fichier

        
    try:
        mime = magic.Magic(mime=True)
        typeoffile = mime.from_file(str(filepath))
        metadatafile['guessed_type'] = typeoffile
    except:
        try:
            typeoffile = guess(str(filepath))
            metadatafile['guessed_type'] = typeoffile
        except :
            metadatafile['guessed_type'] = 'broken'

    return metadatafile

# fonction de nettoyage des fichiers temporaires
def remove_temp_data(filepath):
    try:
        remove(str(filepath))
    except:
        pass

### POUR EVALUATION AWS ###
# fonction de téléversement (à la française) d'un fichier dans le bucketS3
def saveFileInBucket(nomfichier):
    s3 = boto3.resource('s3')
    s3.Object('filrouge.lmy.s3', nomfichier).upload_file(Filename=nomfichier)
    return True

# fonction de lecture d'un fichier depuis le bucketS3
def readFileInBucket(nomfichier):
    s3 = boto3.resource('s3')
    fichier = s3.Object('filrouge.lmy.s3', nomfichier).get()
    return fichier

