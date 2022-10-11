# 3. Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
# lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
# Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
# ("cijena","naziv","kolicina") (Moze i u dvije linije) Vraća novi nested
# dictionary s ključem "ukupno" i dictionary sa ključem "artikli" i listom
# svih odabranih artikala te "cijena" s ukupnom cijenom računa. (Ne treba
# biti One-liner)
# Ispis: [{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2},
# {"cijena":7,"naziv":"Upaljac","kolicina":1}] -> {‘ukupno’: {‘artikli’:
# [‘Kruh’, ‘Sok’, ‘Upaljac’], ‘cijena’: 57}}

lista_diksnerija = [{"cijena":8,"naziv":"Kruh","kolicina":1}, {"cijena":13,"naziv":"Sok","kolicina":2}, {"cijena":7,"naziv":"Upaljac","kolicina":1}] 
def lis_dic(ld):
    key_cmp = ["cijena","naziv","kolicina"]
    rezultat = {'ukupno': {'artikli':[], 'cijena': 0}}
    if isinstance(ld, list):
        if all([isinstance(x, dict) for x in ld]):
            if all([list(x.keys()) == key_cmp for x in ld]):
                for x in ld:
                    rezultat['ukupno']['artikli'].append(x['naziv'])
                    rezultat['ukupno']['cijena'] +=  x['kolicina'] * x['cijena']
                return rezultat
    return 'error'

print(lis_dic(lista_diksnerija))