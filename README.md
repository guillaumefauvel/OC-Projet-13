## Résumé

Site web d'Orange County Lettings

# Développement local

## Prérequis

- Un compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- L'interpréteur Python, version 3.6 ou supérieure
- Docker

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

## macOS / Linux  

### Cloner le repository

- `git clone https://github.com/guillaumefauvel/OC-Projet-13.git`

### Créer l'environnement virtuel

- `cd /path/to/app-folder`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement : `source venv/bin/activate`
- Vérifiez que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Vérifiez que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Vérifiez que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

### Exécuter le site

- `cd /path/to/app-folder`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Vérifiez que le site fonctionne correctement et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

### Lancement des différents process

*Tous les process doivent être lancer dans le dossier propre au projet et l'environnement virtuel doit être activé.*

Lancez le linting avec la commande : `flake8` 

Les test unitaires : `pytest`  

Les tests fonctionnels avec un `python manage.py test`.  
Si vous recevez un message d'erreur, vous devez probablement télécharger Chrome ou changer le driver présent au sein du dossier **`dependencies`**. Veillez à conserver la version propre à l'image docker ( **`linux_chromedriver`** ) et à intégrer la version de votre navigateur locale au sein du code `oc_lettings_site/test.py` -> function `setUpClass`.

Pour vérifier la couverture des tests insérez cette suite de commande :
1. `coverage run -m pytest`
2. `coverage report`
3. `coverage html`

### Base de données

- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

## Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Lancer le dernier build en local avec docker

- `docker run -p 8000:8000 dockervoyager/oc-lettings:latest`
- Rendez-vous à l'adresse : `http://localhost:8000`

# Déploiement

## Prérequis

- Tout les prérequis précèdants
- Un compte DockerHub
- Un compte CircleCi
- Un compte Heroku
- Un compte Sentry

Une fois que vous souhaitez déployer l'application pour la première fois vous allez devoir configurer les différentes dépendances externes. 


### Initialiser votre repository GitHub

A partir de la version clonée créez votre propre repository GitHub à partir de votre version. 

### Configuration de CircleCi

Liiez votre repository GitHub à votre projet CircleCi en appuyant sur le bouton  **`Set Up Project`**. Utilisez la configuration basé sur le fichier config.yml déjà présent dans le repo.  
Dans les variables d'environnement du projet, ajoutez : 

| Clé | Valeur |
| ----------- | ----------- | 
| `DEBUG_STATE` | L'activation du mode debug : `True` ou `False` |
| `SECRET_KEY` | La clez secrète de l'application |
| `DOCKERHUB_USERNAME` | Votre identifiant DockerHub |
| `DOCKERHUB_PASSWORD` | Votre mots de passe DockerHub |
| `DOCKERHUB_REPO` | Le nom de votre repo DockerHub précèdé par l'utilisateur |
| `HEROKU_APP_NAME` | Le nom de l'application Heroku |
| `HEROKU_API_KEY` | La clez API de l'application Heroku |
| `IMAGE_NAME` | Le nom de l'image |
| `SENTRY_DSN` | Le Data Source Name du projet Sentry|

### Configuration de DockerHub


### Configuration d'Heroku



### Configuration de Sentry

Créer un nouveau projet et garder le DSN de ce dernier.

