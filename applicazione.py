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

    scelta = int(input())

    if scelta == 0:
        break

    elif scelta == 1:
        l.visualizza_camere(camere)
    
    input("Premi un tasto per continuare...")
    
print("App chiusa")