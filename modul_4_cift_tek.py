sayi_listesi=list(range(1,21))
cift_sayilar=[]
tek_sayilar=[]

for sayi in sayi_listesi:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)
    else:
        tek_sayilar.append(sayi)

print(tek_sayilar)
print(cift_sayilar)