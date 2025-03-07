# visualizzare info di tutte le camere
def visualizza_camere(camere):
    print(f"{"+":>10}{"-"*70}+")
    print(f"{"|":>10}{"Occupazione":^16}|{"Tipologia":^18}|{"Nominativo":^22}|{"Prezzo(€)":^11}|")
    print(f"{"+":>10}{"-"*70}+")
    count = 0
    while count < len(camere):
        if camere[count]["occupazione"]:
            camere[count]["occupazione"] = "Occupata"
        else:
            camere[count]["occupazione"] = "Non occupata"
            camere[count]["nominativo"] = "Nessun nominativo"

        print(f"Camera {count}:|{camere[count]["occupazione"]:^16}|{camere[count]["tipologia"]:^18}|{camere[count]["nominativo"]:^22}|{camere[count]["prezzo"]:^11d}|")
        count += 1
    print(f"{"-"*9}+{"-"*70}+")

# visualizzare info camere per tipologia in input
def visualizza_tipologia():
    pass

# modifica delle info per camera
def modifica_camera(camere):
    visualizza_camere(camere)
    try:
        scelta=int(input("Quale camera vuoi modificare?(Scegli tramite il numero della camera): "))
    except ValueError:
        print("Dovevi inserire un numero!")
        return
    count = 0
    while count<len(camere):
        if scelta<1 or scelta>len(camere):
            print("Hai sbagliato a scegliere il numero della camera!")
        else:
            tipo_nuova=input("Qual è la nuova tipologia della camera?: ")
            try:
                prezzo_nuovo=int(input("Qual è il nuovo prezzo?: "))
                occupazione=int(input("Metti 0 se l'occupazione è libera e metti 1 se l'occupazione è occupata: "))
            except ValueError:
                print("Inserisci un numero e non una stringa!")
            if occupazione<0 or occupazione>1:
                print("Sbagliato a inserire!")
            elif occupazione==0:
                occupazione_nuova=False
            elif occupazione==1:
                nominativo_nuovo=input("A chi appartiene il nuovo nominativo?: ")
                occupazione_nuova=True
            camere[scelta]={
                "occupazione":occupazione_nuova,
                "tipologia":tipo_nuova,
                "nominativo":nominativo_nuovo,
                "prezzo":prezzo_nuovo
            }
            print("Modificato con successo",camere[scelta])
        return

# eliminare una camera
def elimina_camera():
    pass

