# SIO_2021
# Projet FIL ROUGE
### Hugues LAMY


## Description

Ceci est une application écrite dans le cadre du mastère SIO 2021 de CentraleSupélec, par l'élève Hugues LAMY.
Elle permet de générer un fichier JSON contenant un fichier et ses métadonnées, à partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le développement a été effectué avec VS Code - l'environnement virtuel crée par celui-ci est dans le dossier /venv.

## Installation

Cet outil d'extraction de métadonnées a été developpée sous windows et testé avec la distribution FreeBSD (système recommandé).

Python 3.7, puis les librairies nécessaires doivent être installées. 

Le contenu du fichier zippé doit être dézippé dans le répertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y déposer l'ensemble des scripts python nécessaires.


### python3.7 : 
installation via $ pkg install python37

### pip : 
installation via $ pkg install

### installation des librairies nécessaires :
pip install -r requirements.txt

____________________________________

## Commandes utiles (aide mémoire):
docker container ls

docker stop strange_shockley

docker build -t filrouge .

docker run -p 5555:25252 -v "f:/applicationdata/":/temp filrouge

curl -F file="@test.docx" -X POST http://127.0.0.1:5555/upload

kubectl delete -n default deployment filrouge

kubectl get deployments --all-namespaces

kubectl get pods

# nettoyage du disque avant installation
docker-compose down
docker system prune -a

lancement du container (en 5 exemplaires + nginx comme loadbalancer) via :
docker-compose up --scale filrouge=5 --build filrouge nginx
	
installation de microk8s si kubernetes voulu
sudo snap install microk8s --classic
sudo snap install microk8s --classic --channel=1.18/stable

### récupération de la dernière version de l'application :
git pull https://github.com/hlamy/filrouge main

### construction des images filrouge et nginx :
sudo docker build . -t filrouge
sudo docker build . -t nginx

##

AWS_ACCESS_KEY_ID=$(aws --profile default configure get aws_access_key_id)
AWS_SECRET_ACCESS_KEY=$(aws --profile default configure get aws_secret_access_key)

docker build -t filrouge .
docker run -it --rm \
   -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
   -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY


### Mise en route de l'application ###

L'application peut être lancée via l'execution du script "laucher.py". Aucune autre action n'est nécessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et écrire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5000, c'est à dire par exemple sur http://localhost:5000/ (ou l'adresse IP de la machine serveur suivi de :5000). 

Le bon accès a la page racine http://localhost:5000/ confirme le bon fonctionnement de l'application et donne les informations sur l'API.


## Les contrats API :

/upload/ + requete POST : permet d'envoyer un fichier, les métadonnées et le fichier seront renvoyés en retour dans un format JSON

/ + requête GET : racine, indique si le serveur tourne.


## Requêtes CURL

Voici quelques requêtes CURL utilisables pour atteindre l'application via ses API

#### possible requete CURL pour envoyer un fichier:
curl -u user:password -F file="@test.pdf" -X POST https://filrouge.lmy.p2021.ajoga.fr:5550/upload -k



