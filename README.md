# P9_Developpez_une_application_Web_en_utilisant_Django

Projet numéro 9 du parcour OpenClassrooms "développeur d'application python"

## dépendance

Le projet a été créer en utilisant Python 3.12.

Le projet utilise [Django_tailwind](https://github.com/timonweb/django-tailwind/tree/master)
Pour que le site s'affiche correctement il est nécessaire d'installer Node.js afin de pouvoir utiliser npm.
puis suivre l'installation de django_tailwind.


## installer le projet (Windows)

- Commencer par cloner le projet avec git clone

- A la racine du projet (la ou ce trouve le .git) créer votre environement virtuel :
    ```
    python -m venv .env
    ```
- Activer l'environement virtuel :
  ```
     .env\Scripts\activate
  ```
- Installer toute les dépendance :
    ```
        pip install -r requirements.txt
    ```
- allez au dossier de l'application : 
```
cd LITrevu
```
- Assurer d'avoir installer node.js et d'avoir le bon PATH dans le fichier setting.py à la derniere ligne.(LITRevu/setting.py)

- installer tailwinds : 
```
python manage.py tailwind install
python manage.py tailwind build
```

- (Optionnel) si vous souhaitez utiliser le live serveur pour le css lancer le avec : 
```
python manage.py tailwind start
```
