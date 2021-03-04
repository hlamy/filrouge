# SIO_2021
# Projet FIL ROUGE
# Hugues LAMY


## Description

Ceci est une application écrite dans le cadre du mastère SIO 2021 de CentraleSupélec, par l'élève Hugues LAMY.
Elle permet de générer un fichier JSON contenant un fichier et ses métadonnées, à partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le développement a été effectué avec VS Code - l'environnement virtuel crée par celui-ci est dans le dossier /venv.

## Installation

Cet outil d'extraction de métadonnées a été developpée sous windows et testé avec la distribution FreeBSD (système recommandé).

Python 3.7, puis les librairies nécessaires doivent être installées. 

##
Le contenu du fichier zippé doit être dézippé dans le répertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y déposer l'ensemble des scripts python nécessaire.


# python3.7 : 
installation via $ pkg install python37

# pip : 
installation via $ pkg install

# installation des librairies nécessaires :
pip install -r requirements.txt

## Ou librairie par librairie via :

# flask library, 1.1.2 :
installation via $ pip install flask

# pillow library, 8.0.1:
installation via $ pip install pillow

# celery library, 5.0.5:
installation via $ pip install celery

# pathlib library, 1.0.1
installation via $ pip install pathlib

# paramiko library
installation via $ pip install paramiko

# installation de docker
pkg install docker

# installation de docker-machine
pkg install docker-machine

# installation de virtualbox-ose
pkg install virtualbox-ose


____________________________________

Comamndes utiles:
docker container ls

docker stop strange_shockley

docker build -t filrouge .

docker run -p 5555:25252 -v "f:/applicationdata/":/temp filrouge

curl -F file="@test.docx" -X POST http://127.0.0.1:5555/upload

kubectl delete -n default deployment filrouge

kubectl get deployments --all-namespaces

kubectl get pods

docker-compose up --scale filrouge=2 --build filrouge


##

AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

docker build -t filrouge .
docker run -it --rm \
   -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
   -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY


### Tests ####

Les fichiers restants sont eux indispensables
 pour réaliser les tests de fonctionnement : test_pichandler.py réalise les tests sur les fonctions de pichandler.py alors que test_hlamy_main teste lui l'application web. Le dossier tests et ses sous-dossiers contiennent des données controlées destinées à vérifier le bon retour de l'application lors de l'envoi de ces documents.


### Mise en route de l'application ###

L'application peut être lancée via l'execution du script "laucher.py". Aucune autre action n'est nécessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et écrire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5000, c'est à dire par exemple sur http://localhost:5000/ (ou l'adresse IP de la machine serveur suivi de :5000). 

Le bon accès a la page racine http://localhost:5000/ confirme le bon fonctionnement de l'application et donne les informations sur l'API.


#### Les contrats API : ####

/images/ + requete POST : permet d'envoyer une image sur le serveur. Les formats TIFF, BMP, PNG, JPG, JPEG et TGA sont supportés. un pictureID à 7 chiffres (compris entre 1000000 et 9999999) est renvoyé par l'application.

/ + requête GET : racine, indique si le serveur tourne. Fourni aussi des indications concernant les contrats API.

/images/<pictureID> + requête GET : donne les métadata de l'image considérée dans un fichier au format JSON. Si des données EXIF existent, elles y sont ajoutées. Sinon, seules des métadonnées basiques sont fournies (incluant un identifiant unique d'image généré par l'application ainsi que le chemin pour atteindre le thumbnail).

/thumbnails/<pictureID>.jpg + requête GET : permet de récupérer le thumbnail de l'image demandée. 

/delete/<pictureID> + requête DELETE : permet de supprimer les données issues du traitement d'une image (metadonnées, thumbnail, etc.).


#### Requêtes CURL ####

# Voici quelques requêtes CURL utilisables pour atteindre l'application via ses API :

# possible requete CURL pour envoyer un fichier:
curl -F file="@test.pdf" -X POST http://filrouge.lmy.p2021.ajoga.fr:5555/upload

### 'obsolete'
# possible requete CURL pour récupérer les métadonnées de l'image :
curl http://filrouge.lmy.p2021.ajoga.fr:5000/images/<pictureID>



#### limitations (obsolete, à mettre à jour: ####
- un maximum de 9 millions de fichiers sont envoyables sur l'application (ceci pour rester raisonnable : il est possible d'augmenter cette taille dans le programme si cela est désiré, mais hors des enjeux d'une application scolaire).