from datetime import datetime
import time
def alarme():
    heure_reveil = input("Régler un réveil (HH:MM:SS) :")
    try:
        time.strptime(heure_reveil, "%H:%M:%S")
        return heure_reveil
    except ValueError:
        print("Heure non valide, entrer une heure valide.")
        return alarme()
def afficher_heure(heure_reveil):
    while True:
        now = datetime.now()
        heure_actuel = now.strftime("%H:%M:%S")
        print(heure_actuel, end="\r")  
        time.sleep(1)  
        if heure_actuel == heure_reveil:
            print("\nRéveil ! L'heure est arrivée.")
def horloge():
    heure_debut = input("Entrez l'heure de départ HH:MM:SS :")    
    try:
        h, m, s = map(int, heure_debut.split(':'))
        if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
            print("Heure invalide. Veuillez entrer une heure valide .")
            return
    except ValueError:
        print("Format invalide. Veuillez entrer l'heure au format HH:MM:SS .")
        return 
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
    print ("____MENU____")
    print ("1 : Afficher l'heure actuelle ")
    print ("2 : Régler une heure ")
    print ("3 : Régler une alarme ")
    print ("4 : Quitter ")
    choix = input("Faites votre choix (1, 2, 3, 4) : ")
    if choix == "1" :
        print("\nIl est actuellement :")
        afficher_heure(None)
    elif choix == "2" :
        print("\nEntrée l'heure de votre choix :")
        horloge()
    elif choix == "3" :
        heure_reveil = alarme()
        afficher_heure(heure_reveil)
    elif choix == "4" :
        print("Au revoir !")
        exit()
    else:
        print("Choix invalide. Essayez à nouveau.")
menu()