import time

# affiche l'heure
def afficher_heure():
    heure_actuelle = time.strftime("%H:%M:%S", time.localtime())
    print(f"L'heure actuelle est : {heure_actuelle}", end="\r")
    return heure_actuelle

# mettre a jour l'heure et gerer l'alarme
def mettre_a_jour_heure_avec_alarme(alarme):
    try:
        while True:
            heure_actuelle = afficher_heure()  # AFficher l'heure
            if heure_actuelle == alarme:
                print(f"\n⏰ ALARME ! L'heure actuelle ({heure_actuelle}) correspond à l'alarme !")
                break
            time.sleep(1)  
    except KeyboardInterrupt:
        print("\nProgramme arrêté.")

# alarme
def regler_alarme():
    while True:
        alarme = input("Réglez l'alarme au format hh:mm:ss : ")
        try:
            time.strptime(alarme, "%H:%M:%S")  
            return alarme
        except ValueError:
            print("Format invalide. Veuillez réessayer.")

# programme principal
if __name__ == "__main__":
    print("Bienvenue dans le programme d'horloge avec alarme.")
    alarme = regler_alarme()
    print(f"Alarme réglée pour {alarme}.")
    mettre_a_jour_heure_avec_alarme(alarme)

