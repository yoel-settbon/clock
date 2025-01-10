from datetime import datetime  
import time  
import os  
from time import sleep 

def alarme():
    # Demande à l'utilisateur de régler une alarme avec le format HH:MM:SS AM/PM
    heure_reveil = input("Régler un réveil (HH:MM:SS AM/PM) :")
    
    try:
        # Vérifie si l'heure entrée est bien dans le format 12h AM/PM
        time.strptime(heure_reveil, "%I:%M:%S %p")
        return heure_reveil  # Si c'est valide, retourne l'heure entrée
    except ValueError:
        # Si l'heure est invalide, on affiche un message d'erreur et on redemande l'entrée
        print("Heure non valide, entrer une heure valide.")
        return alarme()  # Relance la fonction pour demander à nouveau l'heure

def afficher_heure(heure_reveil):
    while True:
        # Récupère l'heure actuelle du système
        now = datetime.now()
        # Formate l'heure actuelle au format 12h AM/PM
        heure_actuel = now.strftime("%I:%M:%S %p")  
        
        # Affiche l'heure actuelle en réécrasant la ligne précédente (pour afficher une horloge en temps réel)
        print(heure_actuel, end="\r")  
        
        # Attend 1 seconde avant de réactualiser l'heure
        time.sleep(1)  
        
        # Si l'heure actuelle correspond à l'heure de l'alarme, affiche un message
        if heure_actuel == heure_reveil:
            print("\nDebout, FEIGNAAAAASSEEEE")

def horloge():
    # Demande à l'utilisateur d'entrer une heure de départ au format HH:MM:SS
    heure_debut = input("Entrez l'heure de départ HH:MM:SS :")    
    
    try:
        # Découpe l'heure entrée par l'utilisateur en heures, minutes et secondes
        h, m, s = map(int, heure_debut.split(':'))
        
        # Vérifie si l'heure, les minutes et les secondes sont valides
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            print("Heure invalide. Veuillez entrer une heure valide .")
            return  # Si l'heure est invalide, on quitte la fonction
    except ValueError:
        # Si l'entrée n'est pas au bon format (par exemple "12:60:00"), on affiche une erreur
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS .")
        return  # On quitte la fonction en cas d'erreur
    
    while True:
        # Crée une date avec l'heure actuelle, mais en remplaçant l'heure, les minutes et les secondes par celles de l'utilisateur
        heure_formatee = datetime.now().replace(hour=h, minute=m, second=s).strftime("%I:%M:%S %p") 
        
        # Affiche l'heure formatée
        print(heure_formatee, end='\r')
        
        # Attend 1 seconde avant de réactualiser l'affichage
        time.sleep(1)
        
        # Incrémente les secondes
        s += 1
        # Si les secondes atteignent 60, on les remet à 0 et on incrémente les minutes
        if s == 60:
            s = 0
            m += 1
        # Si les minutes atteignent 60, on les remet à 0 et on incrémente les heures
        if m == 60:
            m = 0
            h += 1
        # Si les heures atteignent 24, on les remet à 0
        if h == 24:
            h = 0

def menu():
    while True:  # Ce "while True" permet de garder le menu affiché jusqu'à ce que l'utilisateur choisisse de quitter
        print("______MENU_DE_L'HORLOGE______")
        print("1 : Afficher l'heure actuelle ")
        print("2 : Régler une heure ")
        print("3 : Régler une alarme ")
        print("4 : Quitter ")
        print("_____________________________")
        
        # Demande à l'utilisateur de faire un choix dans le menu
        choix = input("Faites votre choix (1, 2, 3, 4) : ")
        
        sleep(1)  # Pause d'une seconde avant de continuer
        os.system('cls')  # Nettoie l'écran pour réafficher le menu (fonction spécifique à Windows)

        # Si l'utilisateur choisit "1", affiche l'heure actuelle
        if choix == "1":
            print("\nIl est actuellement :")
            afficher_heure(None)  # Affiche l'heure actuelle sans définir d'alarme
        # Si l'utilisateur choisit "2", lui permet de régler une horloge
        elif choix == "2":
            print("\nVous êtes le maître du temps, choisissez l'heure que vous voulez :")
            horloge()  # Lance la fonction horloge pour régler une nouvelle heure
        # Si l'utilisateur choisit "3", lui permet de régler une alarme
        elif choix == "3":
            heure_reveil = alarme()  # Lance la fonction alarme pour régler l'heure de l'alarme
            afficher_heure(heure_reveil)  # Affiche l'heure actuelle et attend l'alarme
        # Si l'utilisateur choisit "4", quitte le programme
        elif choix == "4":
            print("Au revoir !")
            exit()  # Quitte le programme
        else:
            # Si l'utilisateur fait un choix invalide, on lui demande de recommencer
            print("Choix invalide. Essayez à nouveau.")

# Appelle la fonction menu pour démarrer le programme
menu()
