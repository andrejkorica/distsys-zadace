# 5. Funkcija prima listu tuple-a o studentima (id, ime, prezime). Vraća novu
# sortiranu po id-u (manji->veci) listu dictionary-a o studentima kojima ime
# i prezime počinje istim slovom. (One-liner u return-u)
# Ispis : [(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]
# -> [{‘id’: 31, ‘ime’: ‘Marija’, ‘prezime’: ‘Maric’}, {‘id’: 121, ‘ime’:
# ‘Ivan’, ‘prezime’: ‘Ivic’}]

lista_tupli = [(121,"Ivan","Ivic"),(431,"Pero","Horvat"),(31,"Marija","Maric")]

def sort_listu(lt):
    return sorted([{'id': x[0], 'ime': x[1], 'prezime': x[2]} for x in lt if x[1][0] == x[2][0]], key= lambda x: x['id']) 

print(sort_listu(lista_tupli))