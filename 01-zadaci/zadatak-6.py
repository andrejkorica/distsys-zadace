# Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
# ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
# Vraća se spojena lista ili dictionary.
# Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]
# Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}

lista1 =[1,2,1,2]
lista2 = [3,2]

rijecnik1 = {1:2,3:2}
rijecnik2 = {5:2,4:1}

def fuse_ld(ld1, ld2):
    if type(ld1) == type(ld2):
        if isinstance(ld1, dict):
            return ld1 | ld2
        elif isinstance(ld1, list):
            return ld1 + ld2
    return 'error'

print(fuse_ld('a', lista2))
print(fuse_ld(rijecnik1, rijecnik2))