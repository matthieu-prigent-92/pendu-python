"""Jeu du pendu sous Python

But du jeu : Un mot de 8 lettres maximum est à trouver
en essayant de découvrir toutes les lettres qui le composent.
Vous avez 8 chances pour trouver le mot, au delà, vous perdez.
Votre score sera le nombre de chances qu'il vous restera une fois
le mot découvert.

Bonne partie !"""
# initialisation des imports
import os
from donnees import *
from fonctions import *

# chargement des scores
scores = recup_scores()

# identification du joueur
joueur = recup_joueur()
joueur_present = False
score_joueur = 0

for cle, valeur in scores.items():
    if cle == joueur:
        score_joueur = valeur
        joueur_present = True
        print("Vous avez déjà joué auparavant, votre score est de {}.".format(valeur))
if joueur_present == False:
    scores[joueur] = score_joueur

# démarrage de la partie
continuer = True
while continuer is not False:
    i = nb_chances
    # print("Vous avez {} chances.".format(i))
    
    # sélection du mot par l'ordinateur
    mot = choisir_mot()
    lettres_trouvees = []
    mot_masque = recup_mot_masque(mot, lettres_trouvees)
    
    # lancement du pendu
    sortir = False
    while (sortir is not True):
        # On affiche le mot avec les lettres trouvées
        print("Voici le mot à trouver : {} ({} chances)".format(mot_masque, i))

        # on demande à l'utilisateur de saisir la lettre
        lettre = recup_lettre()
        if lettre in lettres_trouvees:
            print("Vous avez déjà saisi cette lettre.\n")
        elif lettre in mot:
            print("Bien joué ! vous avez trouvé une lettre !\n")
            lettres_trouvees.append(lettre)
        else:
            i -= 1
            lettres_trouvees.append(lettre)
            print("Dommage ! la lettre '{}' n'est pas présente.\n".format(lettre))
            # print("Il vous reste {} chances.\n".format(i))
        mot_masque = recup_mot_masque(mot, lettres_trouvees)
        # test si le mot est trouvé
        if mot == mot_masque:
            # si oui, le score est enregistré
            score_joueur += i
            print("Bravo ! Vous avez trouvé le mot {} en {} coups.".format(mot_masque, i))
            print("Vous gagnez donc {} points, votre score s'élève à {}.\n".format(i, score_joueur))
            
            # on sort de la 2nde boucle
            sortir = True
            
        # L'utilisateur est sorti naturellement de la boucle,
        # il a donc perdu
        if i == 0:
            print("Pendu ! Vous n'avez pas réussi à trouver le mot.")
            print("Le mot était : {}".format(mot))
            print("Vous ne marquez pas de points, votre score reste à {}.\n".format(score_joueur))
            sortir = True
    
    # on demande l'utilisateur s'il veut rejouer
    quitter = input("Voulez-vous rejouer ? (O/N) ")
    if quitter == 'n':
        continuer = False
        scores[joueur] = score_joueur
        enregistrer_scores(scores)

os.system("pause")
