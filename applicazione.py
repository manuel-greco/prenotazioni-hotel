import os
import libreria as l

camere = [
    {
        "occupazione": True,
        "tipologia": "singola",
        "nominativo": "Marco Ferrari",
        "prezzo": 80
    },
    {
        "occupazione": True,
        "tipologia": "doppia",
        "nominativo": "Giulia Russo",
        "prezzo": 120
    },
    {
        "occupazione": False,
        "tipologia": "doppia",
        "nominativo": "",
        "prezzo": 120
    },
    {
        "occupazione": False,
        "tipologia": "tripla",
        "nominativo": "",
        "prezzo": 140
    },
    {
        "occupazione": True,
        "tipologia": "suite",
        "nominativo": "Andrea Ricci",
        "prezzo": 220
    }
]


while True:
    os.system('cls')
    print("0. Esci")
    print("1. Visualizza tutte le camere")
<<<<<<< HEAD
    print("2. Modifica una camera ")
=======
    print("2. Visualizza camere per tipologia")
    
    print("4. Elimina una camera")
>>>>>>> a3318ec1e1320071becd0462f53863f127be5e9f
    print("4. Crea una nuova camera")
    print("5. Elimina una camera")

    scelta = int(input())

    if scelta == 0:
        break

    elif scelta == 1:
        l.visualizza_camere(camere)
<<<<<<< HEAD
    elif scelta==2:
        l.modifica_camera(camere)
=======
    elif scelta == 2:
        l.visualizza_tipologia(camere)
        
    elif scelta == 4:
        l.crea_camera(camere)  
    elif scelta == 5:
        l.elimina_camera(camere) 
        
    
>>>>>>> a3318ec1e1320071becd0462f53863f127be5e9f
    input("Premi un tasto per continuare...")
    
print("App chiusa")