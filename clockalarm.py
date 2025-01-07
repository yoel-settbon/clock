from datetime import datetime
import time
import pygame  # Importer pygame pour jouer des fichiers audio
pygame.init()

# Charger le son de l'alarme
alarme_sound = pygame.mixer.Sound("alarm.wav")

def alarme():
    """Permet à l'utilisateur de régler une alarme."""
    heure_reveil = input("Régler un réveil (HH:MM:SS) : ")
    try:
        # Vérifier si l'heure entrée est valide
        time.strptime(heure_reveil, "%H:%M:%S")
        return heure_reveil
    except ValueError:
        print("Heure non valide, entrer une heure valide.")
        return alarme()

def afficher_heure(heure_reveil=None):
    """Affiche l'heure et joue l'alarme lorsque l'heure de réveil est atteinte."""
    while True:
        now = datetime.now()
        heure_actuel = now.strftime("%H:%M:%S")
        print(heure_actuel, end="\r")  
        time.sleep(1)  

        # Vérifier si l'heure actuelle correspond à l'heure de réveil
        if heure_reveil and heure_actuel == heure_reveil:
            print("\nRéveil ! L'heure est arrivée.")
            alarme_sound.play()  # Jouer l'alarme

def horloge():
    """Affiche l'heure à partir de l'heure de départ et incrémente les secondes."""
    heure_debut = input("Entrez l'heure de départ HH:MM:SS :")    
    try:
        h, m, s = map(int, heure_debut.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            print("Heure invalide. Veuillez entrer une heure valide.")
            return
    except ValueError:
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS .")
        return 

    # Afficher l'heure et incrémenter les secondes
    while True:
        print(f"{h:02}:{m:02}:{s:02}", end='\r')
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

def menu():
    """Affiche le menu principal pour naviguer dans les options."""
    while True:
        print ("____MENU____")
        print ("1 : Afficher l'heure actuelle ")
        print ("2 : Régler une heure ")
        print ("3 : Régler une alarme ")
        print ("4 : Quitter ")
        choix = input("Faites votre choix (1, 2, 3, 4) : ")
        
        if choix == "1" :
            print("\nIl est actuellement :")
            afficher_heure()  # Afficher l'heure sans réglage d'alarme
        elif choix == "2" :
            print("\nEntrée l'heure de votre choix :")
            horloge()
        elif choix == "3" :
            heure_reveil = alarme()  # Demander l'heure de l'alarme
            afficher_heure(heure_reveil)  # Afficher l'heure avec l'alarme
        elif choix == "4" :
            print("Au revoir !")
            break  # Quitter le programme
        else:
            print("Choix invalide. Essayez à nouveau.")

# Lancer le menu principal
menu()
