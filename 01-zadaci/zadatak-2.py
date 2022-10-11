# 2. Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne
# error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
# liste tipa integer. Vraća novi dictionary, gdje je value element iz liste na
# tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.
# Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}

lista = [8,7,1]
rijecnik = {1:2,2:1,3:2}

def dic_list (l, d):
    if isinstance(l, list) and isinstance(d, dict):
        if len(l) == len (d):
            if all([isinstance(x, int) for x in l]):
                return {(k+1):(v if v in range(5, 10) else -1) for k,v in enumerate(l)}
    return 'error'

print(dic_list(lista, rijecnik))