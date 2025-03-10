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
    print(f'{"-"*50}+')
    print(f'|{"Benvenuto nel Hotel":^50}|')
    print(f'+{"-"*50}+')
    print(f'|0. Esci{"|":>44}')
    print(f'|1. Visualizza tutte le camere{"|":>22}')
    print(f'|2. Visualizza camere per tipologia{"|":>17}')
    print(f'|3. Modifica una camera{"|":>29}')
    print(f'|4. Crea una nuova camera{"|":>27}')
    print(f'|5. Elimina una camera{"|":>30}')
    print(f'|6. Prenota una camera{"|":>30}')
    print(f'+{"-"*50}+')
<<<<<<< HEAD
    scelta = int(input("\033[92mSeleziona la tua scelta: ]"))
=======
    try:
        scelta = int(input("\033[92mSeleziona la tua scelta: \033[0m"))
    except ValueError:
        print("\033[41;37mInserisci un numero e non una stringa!\033[0m")
        input("\033[93mPremi un tasto per continuare...")
>>>>>>> a5aafe4f1e7af8e9f8a5efb360c018ed20f44d6c

    if scelta == 0:
        break

    elif scelta == 1:
        l.visualizza_camere(camere)

    elif scelta==2:
        l.visualizza_tipologia(camere)

    elif scelta==3:
        l.modifica_camera(camere)

    elif scelta == 4:
        l.crea_camera(camere)

    elif scelta == 5:
        l.elimina_camera(camere)

    elif scelta == 6:
        l.prenota_camera(camere)
        
<<<<<<< HEAD
    input("\033[93mPremi un tasto per continuare...]")
    
print("\033[41mApp chiusa]")
=======
    input("\033[93mPremi un tasto per continuare...\033[0m")
    
print("\033[41mApp chiusa\033[0m")
>>>>>>> a5aafe4f1e7af8e9f8a5efb360c018ed20f44d6c
