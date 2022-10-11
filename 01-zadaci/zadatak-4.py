# Funkcija prima dvije liste, provjerava dal su istih duljina, ako nisu raise-a
# Error. Vraća novu listu uspoređujući elemente na istim indeksima. Ako
# su vrijednosti iste, vraća taj element, ako nisu vraća -1 na toj poziciji.
# (Funkcija mora imati dvije linije)
# Ispis: [1,2,3,4,5],[2,2,4,4,5] -> [-1, 2, -1, 4, 5]

lista1 = [1,2,3,4,5]
lista2 = [2,2,4,4,5]

def lista_lista(l1, l2):
    return [x if x==l2[i] else -1 for i, x in enumerate(l1)] if len(l1) == len(l2) else "error" 

print(lista_lista(lista1, lista2))