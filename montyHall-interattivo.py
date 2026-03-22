import random

porte = [1, 2, 3]

if __name__ == "__main__":
    auto = random.choice(porte)

    try:
        while True:
            try:
                scelta = int(input("Inserisci un numero da 1 a 3: "))
                if scelta in porte:
                    break
                print("Valore fuori range. Inserisci un numero tra 1 e 3.")
            except ValueError:
                print("Tipo non valido. Inserisci un numero intero.")

        print(f"Hai scelto la porta: {scelta}")

        porte_apribili = [p for p in porte if p != auto and p != scelta]
        porta_capra = random.choice(porte_apribili)
        print(f"Il conduttore apre la porta {porta_capra} e contiene una capra\n")

        while True:
            cambio = input("Sono rimaste due porte, vuoi tenere quella che hai scelto o vuoi cambiare? (tengo/cambio): ")
            if cambio in ('tengo', 'cambio'):
                break
            print("Risposta non valida. Scrivi 'tengo' oppure 'cambio'.")

        if cambio == 'tengo':
            if auto == scelta:
                print("Hai vinto!\n")
            else:
                print(f"Hai perso... L'auto era in {auto}\n")
        elif cambio == 'cambio':
            if auto == scelta:
                print(f"Hai perso... L'auto era in {auto}\n")
            else:
                print("Hai vinto!\n")

    except KeyboardInterrupt:
        print("\nPartita interrotta...")
