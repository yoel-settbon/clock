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
heure_reveil = alarme()
afficher_heure(heure_reveil)
