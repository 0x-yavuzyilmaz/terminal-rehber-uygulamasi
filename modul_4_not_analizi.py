notlar = [88, 92, 75, 42, 99, 53, 77, 85, 60]

#Görevin A Kısmı: Geçen Öğrencileri Bulmak
#geleneksel yöntem ile

gecen_notlar_dongu = []

for ogrenci_notu in notlar:
    if ogrenci_notu >= 60:
        gecen_notlar_dongu.append(ogrenci_notu)

print(gecen_notlar_dongu)


#pythonic yöntem ile

gecen_notlar_comp = [notlar for notlar in notlar if notlar >= 60 ]
print(gecen_notlar_comp)

#Görevin B Kısmı: Notları Yükseltmek (Dönüştürme)

yukseltilmis_notlar = [(notlar +5) for notlar in notlar]
print(yukseltilmis_notlar)

#Görevin C Kısmı: Kalan Öğrencilere Bir Şans (Filtreleme ve Dönüştürme)


kalanlar_icin_sartli_notlar = [(notlar + 5) for notlar in notlar if  notlar < 60]
print(kalanlar_icin_sartli_notlar)