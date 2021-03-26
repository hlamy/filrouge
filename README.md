# SIO_2021
# Projet FIL ROUGE
### Hugues LAMY


## Description

Ceci est une application �crite dans le cadre du mast�re SIO 2021 de CentraleSup�lec, par l'�l�ve Hugues LAMY.
Elle permet de g�n�rer un fichier JSON contenant un fichier et ses m�tadonn�es, � partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le d�veloppement a �t� effectu� avec VS Code - l'environnement virtuel cr�e par celui-ci est dans le dossier /venv.

## Installation

Cet outil d'extraction de m�tadonn�es a �t� developp�e sous windows et test� avec la distribution FreeBSD (syst�me recommand�).

Python 3.7, puis les librairies n�cessaires doivent �tre install�es. 

Le contenu du fichier zipp� doit �tre d�zipp� dans le r�pertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y d�poser l'ensemble des scripts python n�cessaires.


### python3.7 : 
installation via $ pkg install python37

### pip : 
installation via $ pkg install

### installation des librairies n�cessaires :
pip install -r requirements.txt

____________________________________

## Commandes utiles (aide m�moire):
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

### r�cup�ration de la derni�re version de l'application :
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

L'application peut �tre lanc�e via l'execution du script "laucher.py". Aucune autre action n'est n�cessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et �crire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5000, c'est � dire par exemple sur http://localhost:5000/ (ou l'adresse IP de la machine serveur suivi de :5000). 

Le bon acc�s a la page racine http://localhost:5000/ confirme le bon fonctionnement de l'application et donne les informations sur l'API.


## Les contrats API :

/upload/ + requete POST : permet d'envoyer un fichier, les m�tadonn�es et le fichier seront renvoy�s en retour dans un format JSON

/ + requ�te GET : racine, indique si le serveur tourne.


## Requ�tes CURL

Voici quelques requ�tes CURL utilisables pour atteindre l'application via ses API

#### possible requete CURL pour envoyer un fichier:
curl -u user:password -F file="@test.pdf" -X POST https://filrouge.lmy.p2021.ajoga.fr:5550/upload -k



