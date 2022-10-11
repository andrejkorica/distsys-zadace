# 1. Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
# Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
# linije)
# Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]

def string_check(l):
    return [x for x in l if isinstance(x, str) and len(x) > 4] if all([isinstance(x, str) for x in l]) else "error" 

lista = ['Pas', 'Macka', 'Stol']
print(string_check(lista))