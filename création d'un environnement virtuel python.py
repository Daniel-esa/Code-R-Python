# création d'un environnement virtuel sur power shell

#
# py -X.XX -m venv .nom_de_l'environnement
# .test_environnement_virtuel\Scripts\Activate.ps1 # activation de l'environnement
#deactivate me fait repasser au python globale

# Bonne pratique
# Ecrire un fichier texte (nommé requirements.txt en général) avec les spécifications de packages voulues
# Créer un environnement virtuel et l'activer
# Installer les packages indiqués dans le fichier requirements.txt :
# $ (.venv) pip install –r requirements.txt
# Pour créer un fichier de requirements à partir d'un environnement existant :
# $ (.venv) pip freeze > requirements.txt
