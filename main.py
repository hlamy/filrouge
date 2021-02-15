# coding=UTF-8
# importation de l'API
import flaskroutes
from pathlib import Path
import settings
import os
# obtient les paramêtres nécessaires au bon fonctionnement de l'application
applicationportnumber = settings.applicationportnumber
temporary_files_folder = settings.temporary_files_folder

# creation des dossiers nécessaires au travail de l'application si ceux-ci ne sont pas déjà présent
try:
    os.mkdir(temporary_files_folder)
except:
    pass

# lancement du serveur flask et de l'application :
flaskroutes.app.run(host= '0.0.0.0', port=int(applicationportnumber))