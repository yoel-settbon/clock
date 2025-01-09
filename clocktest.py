from datetime import datetime, time as dt_time
import time
import os
from time import sleep
import pygame  # Importer pygame pour jouer des fichiers audio
pygame.init()

alarme_sound = pygame.mixer.Sound("alarm.wav")

def alarme():
    heure_reveil = input("Régler un réveil (HH:MM:SS) : ")
    try:
        # Convertir l'entrée en objet datetime.time
        h, m, s = map(int, heure_reveil.split(':'))
        return dt_time(h, m, s)
    except ValueError:
        print("Heure non valide, veuillez entrer une heure au format HH:MM:SS.")
        return alarme()

def afficher_heure(heure_reveil):
    try:
        while True:
            now = datetime.now()
            heure_actuelle = now.time()  # Obtenir uniquement l'heure actuelle (objet time)
            affichage = now.strftime("%A %d %m %Y --- %I:%M:%S %p ---")  # Format AM/PM
            print(affichage, end="\r")
            time.sleep(1)

            if heure_reveil and heure_actuelle >= heure_reveil:  # Comparaison des objets time
                print("\nDebout, FEIGNAAAAASSEEEE !!!!! ")
                alarme_sound.play()
                sleep(16)
                break  # Arrêter la boucle après avoir joué l'alarme

            os.system('cls')
    except KeyboardInterrupt:
        pygame.mixer.stop()
        print("\nAffichage de l'heure interrompu par l'utilisateur. Retour au menu.")

def horloge():
    try:
        heure_debut = input("Entrez l'heure de départ HH:MM:SS :")   
        try:
            h, m, s = map(int, heure_debut.split(':'))
            if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
                print("Heure invalide. Veuillez entrer une heure valide.")
                return
        except ValueError:
            print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS.")
            return 
        
        while True:
            print(f"{h:02}:{m:02}:{s:02}", end="\r")
            time.sleep(1)
            s += 1
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
            if h == 24:
                h = 0
            os.system('cls') 
    
    except KeyboardInterrupt:
        print("\nHorloge interrompue par l'utilisateur. Retour au menu.")
        return # Efface l'écran pour un affichage propre

def menu():
    while True:
        print("____MENU_DE_L'HORLOGE____")
        print("1 : Afficher l'heure actuelle")
        print("2 : Régler une heure")
        print("3 : Régler une alarme")
        print("4 : Quitter")
        print("_________________________")
        choix = input("Faites votre choix (1, 2, 3, 4) : ")
        sleep(1)
        os.system('cls')
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
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Essayez à nouveau.")

menu()
