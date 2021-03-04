# SIO_2021
# Projet FIL ROUGE
# Hugues LAMY


## Description

Ceci est une application �crite dans le cadre du mast�re SIO 2021 de CentraleSup�lec, par l'�l�ve Hugues LAMY.
Elle permet de g�n�rer un fichier JSON contenant un fichier et ses m�tadonn�es, � partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le d�veloppement a �t� effectu� avec VS Code - l'environnement virtuel cr�e par celui-ci est dans le dossier /venv.

## Installation

Cet outil d'extraction de m�tadonn�es a �t� developp�e sous windows et test� avec la distribution FreeBSD (syst�me recommand�).

Python 3.7, puis les librairies n�cessaires doivent �tre install�es. 

##
Le contenu du fichier zipp� doit �tre d�zipp� dans le r�pertoire choisi par l'utilisateur pour faire fonctionner l'application, pour y d�poser l'ensemble des scripts python n�cessaire.


# python3.7 : 
installation via $ pkg install python37

# pip : 
installation via $ pkg install

# installation des librairies n�cessaires :
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
 pour r�aliser les tests de fonctionnement : test_pichandler.py r�alise les tests sur les fonctions de pichandler.py alors que test_hlamy_main teste lui l'application web. Le dossier tests et ses sous-dossiers contiennent des donn�es control�es destin�es � v�rifier le bon retour de l'application lors de l'envoi de ces documents.


### Mise en route de l'application ###

L'application peut �tre lanc�e via l'execution du script "laucher.py". Aucune autre action n'est n�cessaire, mais l'utilisateur doit avoir les droits suffisants pour que le script puisse executer/lire et �crire dans son dossier courant.

Ce script lancera un serveur flask accessible sur le port 5000, c'est � dire par exemple sur http://localhost:5000/ (ou l'adresse IP de la machine serveur suivi de :5000). 

Le bon acc�s a la page racine http://localhost:5000/ confirme le bon fonctionnement de l'application et donne les informations sur l'API.


#### Les contrats API : ####

/images/ + requete POST : permet d'envoyer une image sur le serveur. Les formats TIFF, BMP, PNG, JPG, JPEG et TGA sont support�s. un pictureID � 7 chiffres (compris entre 1000000 et 9999999) est renvoy� par l'application.

/ + requ�te GET : racine, indique si le serveur tourne. Fourni aussi des indications concernant les contrats API.

/images/<pictureID> + requ�te GET : donne les m�tadata de l'image consid�r�e dans un fichier au format JSON. Si des donn�es EXIF existent, elles y sont ajout�es. Sinon, seules des m�tadonn�es basiques sont fournies (incluant un identifiant unique d'image g�n�r� par l'application ainsi que le chemin pour atteindre le thumbnail).

/thumbnails/<pictureID>.jpg + requ�te GET : permet de r�cup�rer le thumbnail de l'image demand�e. 

/delete/<pictureID> + requ�te DELETE : permet de supprimer les donn�es issues du traitement d'une image (metadonn�es, thumbnail, etc.).


#### Requ�tes CURL ####

# Voici quelques requ�tes CURL utilisables pour atteindre l'application via ses API :

# possible requete CURL pour envoyer un fichier:
curl -F file="@test.pdf" -X POST http://filrouge.lmy.p2021.ajoga.fr:5555/upload

### 'obsolete'
# possible requete CURL pour r�cup�rer les m�tadonn�es de l'image :
curl http://filrouge.lmy.p2021.ajoga.fr:5000/images/<pictureID>



#### limitations (obsolete, � mettre � jour: ####
- un maximum de 9 millions de fichiers sont envoyables sur l'application (ceci pour rester raisonnable : il est possible d'augmenter cette taille dans le programme si cela est d�sir�, mais hors des enjeux d'une application scolaire).