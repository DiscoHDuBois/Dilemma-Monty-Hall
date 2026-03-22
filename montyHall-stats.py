import random
import sys

PORTE = [1, 2, 3]

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 10000
    vittorie_tengo = 0
    vittorie_cambio = 0
    partite_tengo = 0
    partite_cambio = 0

    for i in range(n):
        auto = random.choice(PORTE)
        scelta = random.choice(PORTE)
        porte_apribili = [p for p in PORTE if p != auto and p != scelta]
        porta_capra = random.choice(porte_apribili)

        switch = random.choice([1, 2])
        if switch == 1:
            partite_tengo += 1
            if scelta == auto:
                vittorie_tengo += 1
        elif switch == 2:
            partite_cambio += 1
            if scelta != auto:
                vittorie_cambio += 1

    print(f"Partite totali: {n}")
    if partite_tengo > 0:
        print(f"Tengo:  {vittorie_tengo}/{partite_tengo} vittorie ({vittorie_tengo/partite_tengo*100:.2f}%)")
    else:
        print("Tengo:  nessuna partita registrata")
    if partite_cambio > 0:
        print(f"Cambio: {vittorie_cambio}/{partite_cambio} vittorie ({vittorie_cambio/partite_cambio*100:.2f}%)")
    else:
        print("Cambio: nessuna partita registrata")