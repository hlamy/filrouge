# coding=UTF-8
# importation d'unittest pour executer les tests
import unittest
# importation du script à tester sous le nom "appli" pour pouvoir modifier plus tard le nom du fichier principal
import flaskroutes as appli
# utilisation de la librairie 'Path' pour assurer une bonne gestion des chemins de fichiers
from pathlib import Path
# importation de la librairie io pour gérer les fichiers binaires
import io
# importation de la librairie json pour gérer les fichiers métadonnées générés par l'application
import json
from PIL import Image
from requests.auth import _basic_auth_str
from random import randint
from flask import Flask, send_from_directory, request, abort, send_file
import requests

# Ceci est le fichier de test de l'ensemble des fonctions de hlamy_main.py. Il contient des scénarios de tests qui permettent de tester l'ensemble des fonctionnalités et des API de l'application

# définition des dossiers de tests
testsfile_folder = Path('./testfiles')

# definition de l'usager par défaut (une meilleure solution sera à trouver pour la suite)
credential = []

with open('./auth', "r") as filepswd:
    credential = filepswd.readlines()


with open('./auth', "r") as filepswd:
    credential = filepswd.readlines()  
    username = credential[0].rstrip()  
    password = credential[1].rstrip()

server_api_AWS = 'https://lmy.p2021.ajoga.fr:5555/upload'

server_api_DOCKER = 'https://filrouge.lmy.p2021.ajoga.fr:5550/upload'

class TestApplication_filrouge(unittest.TestCase):

    # test vers le serveur AWS
    def testScenarioUploadAWS(self):
        
        
        # Enchainement des tests avec différents formats
        formatlist = ['csv', 'jpg', 'ods', 'xlsx', 'pdf','png', 'docx', 'txt']
        for formattype in formatlist:
            
            headers = {'Authorization': _basic_auth_str(username, password)}  
            # envoi d'un fichier vers le serveur - attente d'une réponse OK - 200
            
            nomfichierdetest = 'test' + '.' + formattype
            testpath = str(testsfile_folder / Path(nomfichierdetest))

            with open(testpath, 'rb') as fichier:
                testfile = {'file': (testpath, fichier, 'multipart/form-data')}
                serverresponse = requests.post(server_api_AWS, files=testfile, verify=False, headers = headers)

            
            # on vérifie qu'on obtient bien un code de réponse "200"
            self.assertEqual(serverresponse.status_code, 200)

            # récupération des métadonnées renvoyées par le serveur
            receivedMetadata = str(serverresponse.text)          

            # verification que l'extension est bien retrouvée dans le fichier de sortie :
            self.assertIn('"generic_given_extension":".'+ formattype, receivedMetadata)

            # verification que le fichier est bien envoyé sur le s3 :
            self.assertIn('"s3":true', receivedMetadata)
            
            serverresponse.close()
    
    # test vers le serveur DOCKER         
    def testScenarioUploadDOCKER(self):
        
        
        # Enchainement des tests avec différents formats
        formatlist = ['csv', 'jpg', 'ods', 'xlsx', 'pdf','png', 'docx', 'txt']
        for formattype in formatlist:
            
            headers = {'Authorization': _basic_auth_str(username, password)}  
            # envoi d'un fichier vers le serveur - attente d'une réponse OK - 200
            
            nomfichierdetest = 'test' + '.' + formattype
            testpath = str(testsfile_folder / Path(nomfichierdetest))

            with open(testpath, 'rb') as fichier:
                testfile = {'file': (testpath, fichier, 'multipart/form-data')}
                serverresponse = requests.post(server_api_DOCKER, files=testfile, verify=False, headers = headers)

            
            # on vérifie qu'on obtient bien un code de réponse "200"
            self.assertEqual(serverresponse.status_code, 200)

            # récupération des métadonnées renvoyées par le serveur
            receivedMetadata = str(serverresponse.text)          

            # verification que l'extension est bien retrouvée dans le fichier de sortie :
            self.assertIn('"generic_given_extension":".'+ formattype, receivedMetadata)

            # verification que le fichier est bien envoyé sur le s3 :
            self.assertIn('"s3":true', receivedMetadata)
            
            serverresponse.close()

# lancement de la procédure de test
if __name__ == '__main__':
    unittest.main()
