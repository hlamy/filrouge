# SIO_2021
# Projet FIL ROUGE
## Hugues LAMY


# Description

Ceci est une application �crite dans le cadre du mast�re SIO 2021 de CentraleSup�lec, par l'�l�ve Hugues LAMY.
Elle permet de g�n�rer un fichier JSON contenant un fichier et ses m�tadonn�es, � partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le d�veloppement a �t� effectu� avec VS Code - l'environnement virtuel cr�e par celui-ci est dans le dossier /venv.

# Installation

Cet outil d'extraction de m�tadonn�es a �t� developp�e sous windows et test� avec la distribution FreeBSD (syst�me recommand�) et GNU/Linux - distribution UBUNTU (si docker).

Python 3.7, puis les librairies n�cessaires doivent �tre install�es. 

Le contenu du fichier zipp� doit �tre d�zipp� dans le r�pertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y d�poser l'ensemble des scripts python n�cessaires.


#### python3.7 : 
installation via $ pkg install python37

#### pip : 
installation via $ pkg install

#### installation des librairies n�cessaires :
pip install -r requirements.txt

____________________________________

## Lancement des tests :

test_main.py et test_flaskroutes.py permettent de lancer les tests automatiques de l'application filrouge. Il demanderont les cr�dentiels d'acc�s au chemin /upload pour pouvoir op�rer.


#### nettoyage du disque avant installation
docker-compose down
docker system prune -a

lancement du container (en 5 exemplaires + nginx comme loadbalancer) via :
docker-compose up --scale filrouge=5 --build filrouge nginx
	
#### r�cup�ration de la derni�re version de l'application :
git pull https://github.com/hlamy/filrouge main

#### construction des images filrouge et nginx :
sudo docker build . -t filrouge
sudo docker build . -t nginx

## Mise en route de l'application :

L'application peut �tre lanc�e via l'execution du script "main.py". Aucune autre action n'est n�cessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et �crire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5555 par d�faut ou sur le port fourni en argument.


## Les contrats API :

/upload/ + requete POST : permet d'envoyer un fichier, les m�tadonn�es et le fichier seront renvoy�s en retour dans un format JSON

/ + requ�te GET : racine, indique si le serveur tourne.


## Requ�te CURL :

Voici une requete CURL utilisable pour atteindre l'application via son API :

#### possible requete CURL pour envoyer un fichier:
curl -u user:password -F file="@test.pdf" -X POST https://filrouge.lmy.p2021.ajoga.fr:5550/upload -k



