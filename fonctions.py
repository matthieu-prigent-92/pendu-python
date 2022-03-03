"""Fichier contenant les fonctions utiles à l'application du jeu du pendu"""

# import des packages
import os
import pickle
from random import choice
from donnees import *


# initialisation des fonctions
def recup_scores():
    """Fonction qui renvoie les scores enregistrées dans le fichier scores
    la valeur retournée est un dictionnaire"""
    if os.path.exists("scores"):
        with open("scores", 'rb') as fichier_scores:
            mon_depickler = pickle.Unpickler(fichier_scores)
            scores = mon_depickler.load()
    else:
        scores = {}
    return scores

def enregistrer_scores(scores):
    """Fonction qui permet d'enregistrer les nouveaux scores des joueurs
    Cette fonction ne renvoie rien"""
    with open("scores", 'wb') as fichier_scores:
        mon_pickler = pickle.Pickler(fichier_scores)
        mon_pickler.dump(scores)

def recup_joueur():
    """Fonction qui renvoie le nom du joueurs
    La valeur retournée est une chaîne de caractères"""
    nom_joueur = input("Entrez votre prénom : ")
    nom_joueur = nom_joueur.capitalize()
    return nom_joueur

def recup_lettre():
    """Fonction qui renvoie la lettre saisie par l'utilisateur
    La valeur retournée est une chaîne de caractères"""
    lettre = input("Entrez votre lettre : ")
    if len(lettre) > 1 or not lettre.isalpha():
        print("Vous n'avez pas saisi une lettre valide")
        return recup_lettre
    else:
        return lettre

def choisir_mot():
    """Fonction qui renvoie le mot choisi aléatoirement par l'application
    La valeur retournée est une chaîne de caractères"""
    return choice(liste_mots)

def recup_mot_masque(mot_complet, lettres_trouvees):
    """Fonction qui renvoie le mot à trouver masqué de "*" selon les lettres trouvées
    Cette fonction prend en argument 
        - une chaîne de caractères "mot_complet"
        - une liste "lettres_trouvees"
    La valeur retournée est une chaîne de caractères"""
    mot = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot += lettre
        else:
            mot += "*"
    return mot

def recup_liste_mots():
    """Fonction qui renvoie les mots enregistrées dans le fichier mots
    la valeur retournée est une liste""" 
    if os.path.exists("mots"): # Le fichier existe
        # On le récupère
        fichier_mots = open("mots", 'rb')
        mon_depickler = pickle.Unpickler(fichier_mots)
        liste = mon_depickler.load()
        fichier_mots.close()
    else: # Le fichier n'existe pas
        liste = []
    return liste

def enregistrer_mot():
    """Fonction qui permet d'enregistrer les nouveaux mots qui seviront pour le jeu
    Cette fonction ne renvoie rien"""
    continuer = True
    liste = recup_liste_mots()
    while continuer is not False:
        mot = input("Entrez votre mot : ")
        liste.append(mot)
        quitter = input("Voulez-vous ajouter un autre mot ? (O/N) ")
        if quitter.lower() == 'n':
            continuer = False
    liste = sorted(liste)
    print(liste)
    fichier_mots = open("mots", 'wb')
    mon_pickler = pickle.Pickler(fichier_mots)
    mon_pickler.dump(liste)
    fichier_mots.close()
