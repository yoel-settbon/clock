from datetime import datetime
import time
def alarme():
    heure_reveil = input("Regler un reveil (HH:MM:SS) :")
    try :
        time.strptime (heure_reveil, "%H:%M:%S")
        return heure_reveil
    except ValueError:
        print("Heure non valide, entrer une heure valide .")
        return alarme()
alarme()
def afficher_heure():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")    
        print(current_time, end="\r")  
        time.sleep(1)
afficher_heure()
