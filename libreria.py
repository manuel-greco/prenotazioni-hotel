# visualizzare info di tutte le camere
def visualizza_camere(camere):
    print(f'{"+":>10}{"-"*70}+')
    print(f'{"|":>10}{"Occupazione":^16}|{"Tipologia":^18}|{"Nominativo":^22}|{"Prezzo(€)":^11}|')
    print(f'{"+":>10}{"-"*70}+')
    count = 0
    while count < len(camere):
        if camere[count]["occupazione"] == True:
            camere[count]["occupazione"] = "Occupata"
        elif camere[count]["occupazione"] == False:
            camere[count]["occupazione"] = "Non occupata"
            camere[count]["nominativo"] = "Nessun nominativo"

        print(f'Camera {count}:|{camere[count]["occupazione"]:^16}|{camere[count]["tipologia"]:^18}|{camere[count]["nominativo"]:^22}|{camere[count]["prezzo"]:^11d}|')
        count += 1
    print(f'{"-"*9}+{"-"*70}+')

# visualizzare info camere per tipologia in input
def visualizza_tipologia(camere):
    print("Le tipologie di camere presenti nel hotel sono i seguenti: singola, doppia, tripla e suite")
    tipologia = input("Inserisci la tipologia di camera che vuoi visuallizare: ")
    print(f'{"+":>10}{"-"*70}+')
    print(f'{"|":>10}{"Occupazione":^16}|{"Tipologia":^18}|{"Nominativo":^22}|{"Prezzo(€)":^11}|')
    print(f'{"+":>10}{"-"*70}+')
    count = 0
    while count < len(camere):
        if camere[count]["tipologia"] == tipologia:
            if camere[count]["occupazione"]:
                camere[count]["occupazione"] = "Occupata"
            else:
                camere[count]["occupazione"] = "Non occupata"
                camere[count]["nominativo"] = "Nessun nominativo"
                
            print(f'Camera {count}:|{camere[count]["occupazione"]:^16}|{camere[count]["tipologia"]:^18}|{camere[count]["nominativo"]:^22}|{camere[count]["prezzo"]:^11d}|')   
        count += 1
    print(f'{"-"*9}+{"-"*70}+')

# modifica delle info per camera
def modifica_camera(camere):
    visualizza_camere(camere)
    try:
        scelta=int(input("Quale camera vuoi modificare?(Scegli tramite il numero della camera): "))
    except ValueError:
        print("\033[41;37mDovevi inserire un numero!\033[0m")
        return
    
    if scelta<0 or scelta>=len(camere):
        print("\033[41;37mHai sbagliato a scegliere il numero della camera!\033[0m")
    else:
        try:
            nominativo_nuovo=input("A chi appartiene il nuovo nominativo?: ")
        except ValueError:
            print("\033[41;37mInserisci nominativo valido!\033[0m")
            return

        if nominativo_nuovo == "":
            print("\033[41;37mCamera non prenotata: nominativo vuoto!\033[0m")
        else:
            camere[scelta]["nominativo"] = nominativo_nuovo
            camere[scelta]["occupazione"] = True
            print("\033[92mCamera prenotata!\033[0m")

# creazione camera
def crea_camera(camere):
    camera = {}
    try:
        occupazione = input("La camera è 'Occupata' o 'Non occupata'?\nInserisci la tua scelta: ")
        tipologia = input("Inserisci la tipologia della camera (singola/doppia/tripla/suite): ")
        nominativo = input("Inserisci il nominativo dell'ospite, se la camera è libera inserisci 'Nessun nominativo': ")
        prezzo = int(input("Inserisci il prezzo della camera: "))
    except ValueError:
        print("\033[41;37mHai inserito dati sbagliati!\033[0m")
        return
    camera["occupazione"] = occupazione
    camera["tipologia"] = tipologia
    camera["nominativo"] = nominativo
    camera["prezzo"] = prezzo
    camere.append(camera)
    print("La camera è stata aggiunta con sucesso!")

# eliminare una camera
def elimina_camera(camere):
    visualizza_camere(camere)#visualizza le camere 
    #qua sotto chiede in input il numero della camera e lo elimina se è presente nella lista delle camere
    while True:
            try:
                indice = int(input("Inserisci il numero della camera da eliminare: "))
                if 0 <= indice < len(camere):
                    camera_eliminata = camere.pop(indice)
                    print(f"Camera {indice} ({camera_eliminata['tipologia']}) eliminata con successo.")
                    break
                else:
                    print("\033[33mIndice non valido. Riprova.\033[0m")
            except ValueError:
                print("Errore: inserire un numero valido.")