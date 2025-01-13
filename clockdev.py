from datetime import datetime   # Importation pour la manipulation du temps
import time                     # Importation pour gérer les pauses
import os                       # Importation des commandes système
from time import sleep          # Importation des pauses pour faire des pause dans le programme
import pygame                   # Importation pour la lecture du fichier .wav
pygame.init()

alarme_sound = pygame.mixer.Sound("alarm.wav") # Définition d'une variable et récupération du fichier .wav


def alarme():
    # demande à l'utilisateur de régler une alarme
    heure_reveil = input("Régler un réveil (HH:MM:SS AM/PM) :")
    try:
    # s'assure que l'heure entrée est au format voulu AM/PM
        return heure_reveil
    except ValueError:
    # si le format est invalide un message d'erreur s'affiche et redemande de rentrer l'heure
        print("Heure non valide, entrer une heure valide.")
        return alarme()


def afficher_heure(heure_reveil):
    # Utilisation try/except pour appliquer un keyinterrupt
    try:
            # Boucle infinie pour afficher l'heure actuelle
        while True:
            # L'heure du système est récupérée et utilisée
            now = datetime.now()
            # Conversion de l'heure en format AM/PM
            heure_actuelle = now.strftime("%I:%M:%S %p")  # Format AM/PM
            print(heure_actuelle, end="\r")  # Affiche l'heure en temps réel
            time.sleep(1)

            # Conditions d'activation de l'alarme
            if heure_reveil and heure_actuelle == heure_reveil:
                # Affichage du message de l'alarme 
                print("\nDebout, FEIGNAAAAASSEEEE")
                # Activation du fichier .wav de l'alarme
                alarme_sound.play()
                # Gestion du temps de l'affichage du message, correspondant à la durée du fichier .wav
                sleep(16)
                break
    except KeyboardInterrupt:
        # Stoppe le son et retourne au menu
        pygame.mixer.stop()
        print("\nAffichage de l'heure interrompu par l'utilisateur. Retour au menu.")
        return


def horloge():
    # l'utilisateur peux rentrer l'heure de départ souhatée
    heure_debut = input("Entrez l'heure de départ HH:MM:SS :")
    try:
            # Permet de séparer l'heure saisie par l'utilisateur au format HH:MM:SS
        h, m, s = map(int, heure_debut.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            # Si l'heure est invalide, on redemande à l'utilisateur de rentrer une heure valide
            print("Heure invalide. Veuillez entrer une heure valide :")
            return horloge()
    except ValueError:
            # Si l'entrée n'est pas au bon format, on affiche un message d'erreur, et on redemande à l'utilisateur d'entrer une heure valide
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS :")
        return horloge()
                # Utilisation d'un try/except autour de la boucle pour mettre en place le keyinterrupt et retour au menu
    try:
        while True:
                # Créé une date avec l'heure actuelle, remplaçant les heures, minutes, et secondes par celles entrées par l'utilisateur
            heure_formatee = datetime.now().replace(hour=h, minute=m, second=s).strftime("%I:%M:%S %p")
                # Affiche l'heure formatée
            print(heure_formatee, end='\r')
                #Actualise l'heure toutes les secondes
            time.sleep(1)
                # Incrémente les secondes
            s += 1
                # Dès que les secondes et minutes atteignent 60, elles sont remises à 0 et on incrémente les minutes et les heures
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
                # Quand les heures atteignent 24, elles sont remises à 0
            if h == 24:
                h = 0
            os.system('cls')  # Efface l'écran pour un affichage propre

    except KeyboardInterrupt:
        print("\nHorloge interrompue par l'utilisateur. Retour au menu.")
        return


def menu():
    while True:
            # Affichage du menu de l'horloge
        print("______MENU_DE_L'HORLOGE______")
        print("1 : Afficher l'heure actuelle ")
        print("2 : Régler une horloge ")
        print("3 : Régler une alarme ")
        print("4 : Quitter ")
        print("_____________________________")
            # Input permettant à l'utilisateur de faire un choix dans le menu
        choix = input("Faites votre choix (1, 2, 3, 4) : ")
        os.system('cls')
            # Une fois le choix fait, l'utilisateur est redirigé vers la fonction correspondante
        if choix == "1":
            print("\nIl est actuellement :")
            afficher_heure(None)
        elif choix == "2":
            print("\nVous êtes le maître du temps, choisissez l'heure que vous voulez :")
            horloge()
        elif choix == "3":
            heure_reveil = alarme()
            afficher_heure(heure_reveil)
        elif choix == "4":
            # Si l'utilisateur choisit de quitter, un message d'au revoir s'affiche et le programme se ferme
            print("Au revoir !")
            exit()
        else:
            print("Choix invalide. Essayez à nouveau.")


# Appelle la fonction menu de l'horloge
menu()