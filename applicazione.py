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
    scelta = int(input("\033[92mSeleziona la tua scelta: ]"))

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
        
    input("\033[93mPremi un tasto per continuare...]")
    
print("\033[41mApp chiusa]")