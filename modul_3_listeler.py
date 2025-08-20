alisveris_listesi = ["ekmek", "süt", "yumurta", "peynir"]
ogrenci_notlari = [85, 92, 78, 64, 92]
karisik_liste = ["Walter", 52, True, 1.82]

print(alisveris_listesi)
print(ogrenci_notlari)
print(karisik_liste)

ilk_urun = alisveris_listesi[0]
print(ilk_urun)

ucuncu_urun = alisveris_listesi[2]

son_urun= alisveris_listesi[-1]

sondan_birinci_urun = alisveris_listesi[-2]

print(f"Alınacak ilk ürün: {ilk_urun}, alınacak son ürün:  {son_urun}")


alisveris_listesi[0] = "badem sütü"

print(f"Alışveris listesinin yeni hali: {alisveris_listesi}")

alisveris_listesi.append("tereyağı")

print(f"Alışveris listesinin ekleme sonrası yeni hali: {alisveris_listesi}")

alisveris_listesi.remove("süt")


print(f"Alışveris listesinin silme sonrası yeni hali: {alisveris_listesi}")


alisveris_listesi.pop(1)

print(f"Alışveris listesinin pop silme sonrası yeni hali: {alisveris_listesi}")
