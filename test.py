from datetime import datetime
import time

# Fonction pour régler un réveil
def alarme():
    heure_reveil = input("Régler un réveil (HH:MM:SS) :")
    try:
        # On vérifie si l'heure est au bon format
        time.strptime(heure_reveil, "%H:%M:%S")
        return heure_reveil
    except ValueError:
        print("Heure non valide, entrer une heure valide.")
        return alarme()

# Fonction pour afficher l'heure actuelle en continu
def afficher_heure(heure_reveil=None):
    while True:
        now = datetime.now()
        heure_actuel = now.strftime("%H:%M:%S")
        print(heure_actuel, end="\r")  # Affiche l'heure sans sauter de ligne
        time.sleep(1)  # Attendre 1 seconde
        
        # Si un réveil est défini, vérifie si l'heure actuelle correspond à l'heure du réveil
        if heure_reveil and heure_actuel == heure_reveil:
            print("\nRéveil ! L'heure est arrivée.")

# Fonction pour afficher le menu et choisir l'option
def menu():
    print("==== MENU ====")
    print("1. Afficher l'heure actuelle")
    print("2. Régler un réveil")
    print("3. Quitter")
    
    # Demande à l'utilisateur de faire un choix
    choix = input("Entrez votre choix (1, 2 ou 3) : ")
    
    if choix == '1':
        # Afficher l'heure actuelle en continu
        print("\nL'heure actuelle est :")
        afficher_heure()
    elif choix == '2':
        # Régler un réveil
        heure_reveil = alarme()
        afficher_heure(heure_reveil)  # Affiche l'heure et vérifie le réveil
    elif choix == '3':
        print("Au revoir !")
        exit()  # Quitte le programme
    else:
        print("Choix invalide. Essayez à nouveau.")
        menu()  # Si l'utilisateur entre un mauvais choix, recommence le menu

# Appel de la fonction du menu
menu()