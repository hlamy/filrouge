# coding=UTF-8
# import pprint
# importation de flask comme serveur web
from flask import Flask, send_from_directory, request, abort, send_file
# utilisation de la librairie os pour gérer les chemins d'accès et la navigation dans les fichiers
import os
# importation de json pour pouvoir lire les fichiers json contenant les métadonnées
import json
import base64
# utilisation de la librairie PIL pour gérer les images
# from PIL import Image as img
# utilisation de la librairie 'Path' pour assurer une bonne gestion des chemins de fichiers
from pathlib import Path
# importation des fonctions de traitement des fichiers
import utilities


app = Flask(__name__)

# récupération des données de configuration
import settings
temporary_files_folder = settings.temporary_files_folder
app.config['UPLOAD_FOLDER'] = temporary_files_folder


# racine de l'application
@app.route('/')
def mainpage():
    greetingmessage = {'Status': 'Server is up and running'}
    return greetingmessage, 200


@app.route('/upload', methods=['POST'])
def uploadfile():
    datafile = {}
    idfile = 'testouille'
    
    # essai de chargement du fichier fourni par le client. Si NOK, retour d'une erreur
    
    try:
       fichierclient = request.files['file']
    except:
        return {'Error' : 'picture upload problem'}, 500
    
    # récupération du nom de fichier
    idfile = str(fichierclient.filename)
    datafile['id'] = idfile

    # sauvegarde du fichier dans S3
    utilities.saveFileInBucket(fichierclient, idfile)

    # sauvegarde du fichier temporairement sur disque
    try:
        fichierclient.save(temporary_files_folder / Path(idfile))
    except:
        fichierclient.close()
        return {'Error' : 'file saving problem'}, 500
    
    # extraction des métadonnées, 
    # puis insertion de celles-ci dans le dictionnaire
    try:
        datafile = utilities.extractgenericmetadata(datafile)
    except:
        return {'Error' : 'could not extract metadata'}, 500
    
    # extraction et encodage du fichier en base 64, 
    # pour insertion dans le dictionnaire datafile
    try:
        datafile = utilities.code64fichier(datafile)
    except:
        return {'Error' : 'could not encode file'}, 500

    # fermeture du fichier
    fichierclient.close()

    # renvoi du dictionnaire sous forme d'un fichier texte JSON
    return datafile