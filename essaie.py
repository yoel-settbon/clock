from datetime import datetime   # importation pour la manipulation du temps
import time                     # importation pour gérer les pauses
import os                       #importation des commandes système
from time import sleep          # importation des pauses pour faire des pause dans le programme

def alarme():

            # demande à l'utilisateur de régler une alarme
    heure_reveil = input("Régler un réveil (HH:MM:SS AM/PM) :")
    try:
            # s'assure que l'heure entrée est au format voulu AM/PM
        time.strptime(heure_reveil, "%I:%M:%S %p")
        return heure_reveil
    except ValueError:
            # si le format est invalide un message d'erreur s'affiche et redemande de rentrer l'heure
        print("Heure non valide, entrer une heure valide.")
        return alarme()

def afficher_heure(heure_reveil):

            # boucle infinie pour afficher l'heure actuelle
    while True:
            # l'heure du système est récupérée et utilisé
        now = datetime.now()
            # converstion de l'heure en format AM/PM
        heure_actuel = now.strftime("%I:%M:%S %p") 
        print(heure_actuel, end="\r")  
        time.sleep(1)
            # si l'heure actuelle correspond à l'heure réglé pour l'alarme, le message voulu s'affiche  
        if heure_actuel == heure_reveil:
            print("\nDebout, FEIGNAAAAASSEEEE")

def horloge():

            # l'utilisateur peux rentrer l'heure de départ souhatée
    heure_debut = input("Entrez l'heure de départ HH:MM:SS :")    
    try:
            # permet de séparer l'heure entrée par l'utilisateur au format HH:MM:SS
        h, m, s = map(int, heure_debut.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            # si l'heure est invalide, on redemande à l'utilisateur de rentrer une heure valide
            print("Heure invalide. Veuillez entrer une heure valide :")
            return horloge() 
    except ValueError:
            # si l'entrée n'est pas au bon format, on affiche un message d'erreur et on redemande à l'utilisateur de rentrer une heure valide
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS :")
        return horloge()     
    while True:
            # creer une date avec l'heure actuelle, remplaçant les heures, les minutes et les secondes par celles de l'utilisateur
        heure_formatee = datetime.now().replace(hour=h, minute=m, second=s).strftime("%I:%M:%S %p") 
            # affiche l'heure formatée
        print(heure_formatee, end='\r')
            # actualise l'heure toutes les secondes
        time.sleep(1)
            # incrémente les second
        s += 1
            # dès que les seconde, minutes atteignent 60, on les remet à 0 et on incrémente les minutes et les heures
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
            # quand les heures atteignent 24, on les remet à 0
        if h == 24:
            h = 0

def menu():
    
            # permet d'afficher le menu de l'horloge
    print ("______MENU_DE_L'HORLOGE______")
    print ("1 : Afficher l'heure actuelle ")
    print ("2 : Régler une heure ")
    print ("3 : Régler une alarme ")
    print ("4 : Quitter ")
    print ("_____________________________")
            # permet à l'utilisateur de faire un choix dans le menu
    choix = input("Faites votre choix (1, 2, 3, 4) : ")
            # une fois le choix fait, on efface l'écran
    sleep(1)
    os.system('cls')
            # une fois le choix fait, ça nous redirige vers la fonction correspondante
    if choix == "1" :
        print("\nIl est actuellement :")
        afficher_heure(None)
    elif choix == "2" :
        print("\nVous êtes le maître du temps, choisissez l'heure que vous voulez :")
        horloge()
    elif choix == "3" :
        heure_reveil = alarme()
        afficher_heure(heure_reveil)
    elif choix == "4" :
            # si l'utilisateur choisit de quitter, un message d'au revoir s'affiche et le programme se ferme
        print("Au revoir !")
        exit()
    else:
        print("Choix invalide. Essayez à nouveau.")

            # rappel la fonction menu de l'horloge
menu()
