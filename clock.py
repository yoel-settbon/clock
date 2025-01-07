import time

def afficher_heure():
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    print(f"L'heure actuelle est : {heure_actuelle}")

afficher_heure()


