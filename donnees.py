"""Fichier contenant les variables nécessaires à l'application du jeu du pendu"""

# import des packages
import os
import pickle

# initialisation des variables
nb_chances = 8 # nombre max de chances autorisées
nom_fichier_scores = "scores" # nom du fichier contenant les scores des joueurs
nom_fichier_mots = "mots" # nom du fichier contenant les mots du jeu

def recup_liste_mots():
    """Fonction qui renvoie les mots enregistrées dans le fichier mots
    la valeur retournée est une liste""" 
    if os.path.exists(nom_fichier_mots): # Le fichier existe
        # On le récupère
        fichier_mots = open(nom_fichier_mots, 'rb')
        mon_depickler = pickle.Unpickler(fichier_mots)
        liste = mon_depickler.load()
        fichier_mots.close()
    else: # Le fichier n'existe pas
        liste = ["bonjour"]
    return liste

liste_mots = recup_liste_mots() # liste des mots disponibles pour le jeu du pendu
#liste_mots = [
#    "Bonjour",
#    "test"
#    ]