# utilities
# coding=UTF-8
# importation de celery pour gérer la concurence
from celery import Celery
# importation de datetime pour obtenir les informations sur l'heure
from datetime import date, datetime
import json
from pathlib import Path
# si besoin de crypto : importation fernet
# from cryptography.fernet import Fernet
import os
import base64
from filetype import guess
import magic

import settings

appcelery = Celery('tasks', broker='redis://localhost', backend='redis://localhost')

temporary_files_folder = settings.temporary_files_folder

# code de création d'ajout dans le fichier json du fichier encodé en base64
@appcelery.task
def code64fichier(datafile):
    idfile = datafile['id']
    with open(temporary_files_folder / Path(idfile), 'rb') as fichier:
        encodedfile = base64.b64encode(fichier.read())
        datafile['file'] = str(encodedfile)
    return datafile


def extractgenericmetadata(datafile):
    # création du chemin du fichier (lorsque stocké dans le dossier temporaire)
    filepath = temporary_files_folder / Path(datafile['id'])

    # donne la taille du fichier
    try:
        size = os.path.getsize(filepath)
    except:
        size = None 
    datafile['size'] = size


    # donne le nom et l'extension du fichier tels qu'envoyés
    try:
        nomfichier, extensionfichier = os.path.splitext(filepath)
        
    except:
        nomfichier = None
        extensionfichier = None

    # ajoute le nom et l'extension dans le dictionnaire
    datafile['name'] = nomfichier
    datafile['given_extension'] = extensionfichier

    # donne la date de derniere modification du fichier
    try:
        time = os.path.getmtime(filepath) 
    except:
        time = None
    
    datafile['datemodified'] = time

    # donne le type du fichier

        
    try:
        mime = magic.Magic(mime=True)
        typeoffile = mime.from_file(str(filepath))
        datafile['guessed_type'] = typeoffile
    except:
        try:
            typeoffile = guess(str(filepath))
            datafile['guessed_type'] = typeoffile
        except :
            datafile['guessed_type'] = 'broken'

    return datafile