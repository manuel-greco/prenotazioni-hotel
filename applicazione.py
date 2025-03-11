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
    print(f'+{"-"*51}+')
    print(f'|{"Benvenuto nel Hotel":^51}|')
    print(f'+{"-"*51}+')
    print(f'| 0. Esci{"|":>44}')
    print(f'| 1. Visualizza tutte le camere{"|":>22}')
    print(f'| 2. Visualizza camere per tipologia{"|":>17}')
    print(f'| 3. Prenota camera{"|":>34}')
    print(f'| 4. Crea una nuova camera{"|":>27}')
    print(f'| 5. Elimina una camera{"|":>30}')
    print(f'+{"-"*51}+')

    scelta = int(input("\033[93mSeleziona la tua scelta: \033[0m"))
    os.system('cls')
    if scelta == 0:
        break

    elif scelta == 1:
        print(f'{'+':>10}{"-"*51}+')
        print(f'{'|':>10}{"Visualizza tutte le camere":^51}|')
        print(f'{'+':>10}{"-"*51}+')
        l.visualizza_camere(camere)

    elif scelta==2:
        print(f'+{"-"*51}+')
        print(f'|{"Visualizza camere per tipologia":^51}|')
        print(f'+{"-"*51}+')
        l.visualizza_tipologia(camere)

    elif scelta==3:
        print(f'{'+':>10}{"-"*51}+')
        print(f'{'|':>10}{"Prenota camera":^51}|')
        print(f'{'+':>10}{"-"*51}+')
        l.prenota_camera(camere)

    elif scelta == 4:
        print(f'+{"-"*51}+')
        print(f'|{"Crea una nuova camera":^51}|')
        print(f'+{"-"*51}+')
        l.crea_camera(camere)

    elif scelta == 5:
        print(f'+{"-"*51}+')
        print(f'|{"Elimina una camera":^51}|')
        print(f'+{"-"*51}+')
        l.elimina_camera(camere)
        
    input("\033[93mPremi un tasto per continuare...\033[0m")
    
print("\033[41mApp chiusa\033[0m")