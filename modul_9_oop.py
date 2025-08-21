class Ogrenci:
    def __init__(self,ad,soyad,numara):
        self.isim = ad
        self.soyad = soyad
        self.numara = numara
        self.devamsizlik = 0

    def kendini_tanit(self):
        return f"Merhaba, ben {self.isim} {self.soyad}. Numaram: {self.numara}."

    def devamsizlik_yap(self):
        self.devamsizlik += 1
        print(f"{self.isim} {self.soyad} devamsızlık yaptı. Toplam devamsızlık: {self.devamsizlik} ")


ogrenci_1 = Ogrenci("Walter", "White", 102)
ogrenci_2 = Ogrenci("Jesse", "Pinkman",909)
ogrenci_3 = Ogrenci("Yavuz", "Yilmaz",701)

print(ogrenci_1.kendini_tanit())
print(ogrenci_2.kendini_tanit())
print(ogrenci_3.kendini_tanit())

ogrenci_2.devamsizlik_yap()
ogrenci_2.devamsizlik_yap()

print(f"Son durumda Jesse'nin devamsızlığı: {ogrenci_2.devamsizlik}")

