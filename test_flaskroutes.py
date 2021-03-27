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


# definition du décorateur pour tester la partie application
def avec_client(f):
    def func(*args, **kwargs):
        with appli.app.test_client() as client:
            return f(*args, client, **kwargs)

    return func

class TestApplication_filrouge(unittest.TestCase):

    # test unitaire de la page principale de l'application
    def test_mainPage(self):
        resultatAttendu = {'Status': 'Server is up and running'}
        self.assertIn(resultatAttendu, appli.mainpage())


    # test de remontée d'erreur, en cas d'envoi de mauvais fichiers par exemple.
    @avec_client
    def testOfErrors(self, client):
        # test de réponse négative si uploads sans authentification (401 = erreur d'authentification)
        with client.post("/upload") as result:
            self.assertEqual(result.status_code, 401)

        headers = {'Authorization': _basic_auth_str(username, password)}   


        # test de réponse négative si uploads avec authentification mais sans fichier
        with client.post("/upload", headers = headers) as result:
            self.assertEqual(result.status_code, 412)



        # test d'envoi d'un fichier simple - doit répondre 200 malgré tout car gérable par l'application
        fakefilename = 'testfile.txt'
        fakefile = b'bourrageJustePourTester'
        testfile = (io.BytesIO(fakefile), fakefilename)
        testdata = {'file': testfile}
        with client.post("/upload", data=testdata, follow_redirects=True,
                         content_type='multipart/form-data', headers = headers) as serverresponse:
            self.assertEqual(serverresponse.status_code, 200)


    # test de scénario complet, d'envoi d'un fichier puis de lecture de ses métadonnées issues de l'application
    
    @avec_client
    def testScenarioUpload(self, client):
        # Enchainement des tests avec différents formats
        formatlist = ['csv', 'jpg', 'ods', 'xlsx', 'pdf','png', 'docx', 'txt']
        for formattype in formatlist:
            
            headers = {'Authorization': _basic_auth_str(username, password)}  
            # envoi d'un fichier vers le serveur - attente d'une réponse OK - 200
            
            nomfichierdetest = 'test' + '.' + formattype
            testpath = str(testsfile_folder / Path(nomfichierdetest))
            with open(testpath, 'rb') as fichier:
                testdata = {'file': (testpath, fichier, 'multipart/form-data')}

            serverresponse = client.post('/upload', data=testdata, follow_redirects=True, headers = headers)

            # on vérifie qu'on obtient bien un code de réponse "200"
            self.assertEqual(serverresponse.status_code, 200)

            # récupération des métadonnées renvoyées par le serveur
            receivedMetadata = str(serverresponse.data.decode("utf-8"))          

            # verification que l'extension est bien retrouvée dans le fichier de sortie :
            self.assertIn('"generic_given_extension":".'+ formattype, receivedMetadata)

            # verification que le fichier est bien envoyé sur le s3 :
            self.assertIn('"s3":true', receivedMetadata)
            serverresponse.close()

# lancement de la procédure de test
if __name__ == '__main__':
    unittest.main()
