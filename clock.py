from datetime import datetime
import time

while True:
    # Obtenir l'heure actuelle
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    # Afficher l'heure sur la même ligne
    print(current_time, end="\r")  
    
    # Attendre une seconde avant de mettre à jour
    time.sleep(1)