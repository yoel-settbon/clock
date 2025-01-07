"""from datetime import datetime
import time

while True:
    # Obtenir l'heure actuelle
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    # Afficher l'heure sur la même ligne
    print(current_time, end="\r")  
    
    # Attendre une seconde avant de mettre à jour
    time.sleep(1)"""

import datetime, time

def set_custom_time():
    """Permet à l'utilisateur de régler une heure personnalisée."""
    while True:
        try:
            user_input = input("Entrez l'heure (HH:MM:SS) : ")
            h, m, s = map(int, user_input.split(":"))
            if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
                return h, m, s
            else:
                print("L'heure doit être comprise entre 00:00:00 et 23:59:59.")
        except ValueError:
            print("Format incorrect. Essayez à nouveau.")

def display_clock(custom_time=None):
    """Affiche une horloge avec l'heure actuelle ou personnalisée."""
    if custom_time:
        hours, minutes, seconds = custom_time
    else:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second

    while True:
        # Afficher l'heure formatée
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
        time.sleep(1)  # Pause d'une seconde

        # Incrémenter l'heure manuellement
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0

# Programme principal
if input("Régler une heure personnalisée ? (o/n) : ").lower() == "o":
    display_clock(set_custom_time())
else:
    display_clock()