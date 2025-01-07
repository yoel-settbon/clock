import datetime, time
import winsound
def afficher_heure(h, m, s):
    return f"{h:02}:{m:02}:{s:02}"
def alarme():
    heure_reveil = input("Regler un reveil (HH:MM:SS) :")
    try :
        time.strptime (heure_reveil, "%H:%M:%S")
        return heure_reveil
    except ValueError:
        print("Heure non valide, entrer une heure valide .")
        return alarme()
alarme()
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
        print(afficher_heure(h, m, s), end='\r')
        time.sleep(1)
        s += 1
        if s == 60:
            s = 0
            m += 1
        elif m == 60:
            m = 0
            h += 1
        elif h == 24:
            h = 0
horloge()