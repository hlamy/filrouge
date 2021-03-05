# coding=UTF-8
# import pprint
# importation de flask comme serveur web
from flask import Flask, send_from_directory, request, abort, send_file
# utilisation de la librairie os pour gérer les chemins d'accès et la navigation dans les fichiers
import os
# importation de json pour pouvoir lire les fichiers json contenant les métadonnées
import json
import uuid
import base64
# utilisation de la librairie PIL pour gérer les images
# from PIL import Image as img
# utilisation de la librairie 'Path' pour assurer une bonne gestion des chemins de fichiers
from pathlib import Path
# importation des fonctions de traitement des fichiers
import utilities
import pictures
import tables
# creation de l'application Flask
app = Flask(__name__)

# récupération des données de configuration
temporary_files_folder = utilities.temporary_files_folder
app.config['UPLOAD_FOLDER'] = temporary_files_folder


# racine de l'application, pour vérification du bon fonctionnement
@app.route('/')
def mainpage():
    greetingmessage = {'Status': 'Server is up and running'}
    return greetingmessage, 200


@app.route('/upload', methods=['POST'])
def uploadfile():
    datafile = {}
    metadatafile = {}
    idfile = 'testouille'
    
    # essai de chargement du fichier fourni par le client. Si NOK, retour d'une erreur
    try:
       fichierclient = request.files['file']
    except:
        return {'Error' : 'picture upload problem'}, 500
    
    randomUID = str(uuid.uuid4())
    # récupération du nom de fichier
    idfilename = str(fichierclient.filename)
    metadatafile['given_name'] = idfilename

    # genere un ID aléatoire unique
    datafile['uuid'] = randomUID

    # sauvegarde du fichier dans S3
    # l'exception est indispensable (au 27 fev 2021) pour gérer le manque de credentials aws dans docker (en cours d'investigation)
    # s3 = True si sauvegarde dans S3 ok, sinon False
    try :
        datafile['s3'] = utilities.saveFileInBucket(fichierclient, randomUID)
    except:
        datafile['s3'] = False

    datafile['s3'] = utilities.saveFileInBucket(fichierclient, randomUID)

    # sauvegarde du fichier temporairement sur disque
    try:
        fichierclient.save(temporary_files_folder / Path(idfile))
        filepath = str(temporary_files_folder / Path(idfile))
    except:
        fichierclient.close()
        return {'Error' : 'file saving problem'}, 500
    
    # extraction des métadonnées, 
    # puis insertion de celles-ci dans le dictionnaire
    try:
        metadatafile = utilities.extractgenericmetadata(datafile, metadatafile, filepath)
    except:
        return {'Error' : 'could not extract metadata'}, 500
    
    # extraction des metadata concernant spécifiquement les images // si erreur, pas grave
    try:
        metadatafile = pictures.extractMetadata(temporary_files_folder / Path(idfile), metadatafile)
    except:
        pass
    

    # extraction des métadata concernant spécifiquement les tableaux
    try:
        medatafile = tables.extractmetadata(medatafile, filepath)
    except:
        pass

    datafile['metadata'] = metadatafile

    # extraction et encodage du fichier en base 64, 
    # pour insertion dans le dictionnaire datafile
    try:
        datafile['data'] = str(utilities.code64fichier(filepath))
    except:
        return {'Error' : 'could not encode file'}, 500


    # fermeture du fichier
    fichierclient.close()
    utilities.remove_temp_data(filepath)

    # renvoi du dictionnaire sous forme d'un fichier texte JSON
    return datafile