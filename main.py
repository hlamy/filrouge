# coding=UTF-8
# importation de l'API
import flaskroutes
# pour gestion des chemins de fichier, import de 'pathlib'
from pathlib import Path
# pour gestion de la création de dossier, import de 'os'
import os
# argparse pour gerer les arguments au lancement
import argparse
# importation de la librairy d'utilitaire de l'application filrouge
import utilities

# récupération du port de l'application via un argument
try:
    parser = argparse.ArgumentParser()
    parser.add_argument("port")
    args = parser.parse_args()
    applicationportnumber = args.port
except:
    applicationportnumber = "5555"

# obtient les paramêtres nécessaires au bon fonctionnement de l'application - ici le dossier temporaire
temporary_files_folder = utilities.temporary_files_folder

# creation des dossiers nécessaires au travail de l'application si ceux-ci ne sont pas déjà présent
try:
    os.mkdir(temporary_files_folder)
except:
    pass

# lancement du serveur flask et de l'application :
flaskroutes.app.run(host= '0.0.0.0', port=int(applicationportnumber))