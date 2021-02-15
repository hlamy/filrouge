# SIO_2021
# Projet FIL ROUGE
# Hugues LAMY


#### Description ####

Ceci est une application �crite dans le cadre du mast�re SIO 2021 de CentraleSup�lec, par l'�l�ve Hugues LAMY.
Elle permet de g�n�rer un fichier JSON contenant un fichier et ses m�tadonn�es, � partir de ce du fichier fourni par l'utilisateur, via une API de type REST.

Le d�veloppement a �t� effectu� avec VS Code - l'environnement virtuel cr�e par celui-ci est dans le dossier /venv.

#### Installation ####

Cet outil de g�n�ration de thumbnail a �t� developp� sous windows et test� avec la distribution "DEBIAN" de GNU/LINUX (syst�me recommand�).

Python 3.8, puis les librairies flask, pillow, celery et pathlib doivent �tre install�es.

# python : python 3.8

# flask library, 1.1.2 :
installation via $ pip install flask

# pillow library, 8.0.1:
installation via $ pip install pillow

# celery library, 5.0.5:
installation via $ pip install celery

# pathlib library, 1.0.1
installation via $ pip install pathlib

Ensuite, le contenu du fichier zipp� doit �tre d�zipp� dans le r�pertoire choisi par l'utilisateur pour faire fonctionner l'application. En pratique, seulement les fichiers "launcher.py", "hlamy_main.py", et "pichandler.py" sont n�cessaires � minima pour faire fonctionner l'application. 

Le lancement de celle-ci verra la cr�ation, s'il n'existent pas d�j�, des dossiers /metadata, /pictures, /temp et /thumbnail. Ceux-ci contiendront les fichiers n�cessaires � l'application.

L'environnement virtuel est pr�sent dans le dossier /venv au besoin.

### Tests ####

Les fichiers restants sont eux indispensables pour r�aliser les tests de fonctionnement : test_pichandler.py r�alise les tests sur les fonctions de pichandler.py alors que test_hlamy_main teste lui l'application web. Le dossier tests et ses sous-dossiers contiennent des donn�es control�es destin�es � v�rifier le bon retour de l'application lors de l'envoi de ces documents.


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
curl -F file="@test.pdf" -X POST http://127.0.0.1:5555/upload

### 'obsolete'
# possible requete CURL pour r�cup�rer les m�tadonn�es de l'image :
curl http://127.0.0.1:5000/images/<pictureID>

# possible requete CURL pour r�cup�rer le thumbnail de l'image, sauvegard� dans le dossier courant :
curl --output <pictureID>.jpg http://127.0.0.1:5000/thumbnails/<pictureID>.jpg


#### limitations : ####

- Les fichiers "texture" ne sont pas pris en compte, ce ne sont pas des formats d'image ;
- Les fichiers "logiciel de retouche" ne sont pas pris en compte, ce ne sont pas des formats d'image ;
- Les fichiers '.gif' ne sont pas compatible avec l'application ;
- un maximum de 9 millions de fichiers sont envoyables sur l'application (ceci pour rester raisonnable : il est possible d'augmenter cette taille dans le programme si cela est d�sir�, mais hors des enjeux d'une application scolaire).