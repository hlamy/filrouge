# SIO_2021
# Projet FIL ROUGE
## Hugues LAMY


# Description

Ceci est une application écrite dans le cadre du mastère SIO 2021 de CentraleSupélec, par l'élève Hugues LAMY.
Elle permet de générer un fichier JSON contenant un fichier et ses métadonnées, à partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le développement a été effectué avec VS Code - l'environnement virtuel crée par celui-ci est dans le dossier /venv.

# Installation

Cet outil d'extraction de métadonnées a été developpée sous windows et testé avec la distribution FreeBSD (système recommandé) et GNU/Linux - distribution UBUNTU (si docker).

Python 3.7, puis les librairies nécessaires doivent être installées. 

Le contenu du fichier zippé doit être dézippé dans le répertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y déposer l'ensemble des scripts python nécessaires.


#### python3.7 : 
installation via $ pkg install python37

#### pip : 
installation via $ pkg install

#### installation des librairies nécessaires :
pip install -r requirements.txt

____________________________________

## Lancement des tests :

test_main.py et test_flaskroutes.py permettent de lancer les tests automatiques de l'application filrouge. Il demanderont les crédentiels d'accès au chemin /upload pour pouvoir opérer.


#### nettoyage du disque avant installation
docker-compose down
docker system prune -a

lancement du container (en 5 exemplaires + nginx comme loadbalancer) via :
docker-compose up --scale filrouge=5 --build filrouge nginx
	
#### récupération de la dernière version de l'application :
git pull https://github.com/hlamy/filrouge main

#### construction des images filrouge et nginx :
sudo docker build . -t filrouge
sudo docker build . -t nginx

## Mise en route de l'application :

L'application peut être lancée via l'execution du script "main.py". Aucune autre action n'est nécessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et écrire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5555 par défaut ou sur le port fourni en argument.


## Les contrats API :

/upload/ + requete POST : permet d'envoyer un fichier, les métadonnées et le fichier seront renvoyés en retour dans un format JSON

/ + requête GET : racine, indique si le serveur tourne.


## Requête CURL :

Voici une requete CURL utilisable pour atteindre l'application via son API :

#### possible requete CURL pour envoyer un fichier:
curl -u user:password -F file="@test.pdf" -X POST https://filrouge.lmy.p2021.ajoga.fr:5550/upload -k



