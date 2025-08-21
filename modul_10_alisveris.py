alisveris_listesi = ["elma", "kavun", "peynir", "ekmek"]

with open("alisveris.txt", "w") as dosya:
    for i in alisveris_listesi:
        dosya.write(f"{i} \n")

print("Bütün ürünler listeye eklendi.")

okunan_liste = []

with open("alisveris.txt", "r") as dosya:
    for satir in dosya:
        okunan_liste.append(satir.strip())

print(okunan_liste)