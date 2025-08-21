# Hayvan ebeveyn nesil oluşturma
class Hayvan:
    def __init__(self, isim, yas):
        print("Hayvan nesnesi oluşturuluyor...")
        self.isim = isim
        self.yas = yas

    def yemek_ye(self):
        print(f" {self.isim} yemek yiyor")

    def ses_cikar(self):
        print(f"{self.isim} ses cikardi.")


class Kedi(Hayvan):
    def tirman(self):
        print(f" {self.isim} ağaca tırmanıyor.")

    def ses_cikar(self):
        print("Miyav!")
        # override



class Kopek(Hayvan):
    def __init__(self, isim, yas, cins):
        super().__init__(isim, yas)
        print("Bir Kopek nesnesi yaratılıyor...")
        self.cins = cins

    def ses_cikar(self):
        print("Hav Hav!")


# --- NESNELERİ KULLANALIM ---

tekir = Kedi("Tekir", 5)

tekir.tirman()
tekir.ses_cikar()
tekir.yemek_ye()

comar = Kopek("Çomar", 5, "Sokak Köpeği")

comar.ses_cikar()
comar.yemek_ye()

civciv = Hayvan("Maşuk", 1)
civciv.ses_cikar()
print(f"Hayvanın adı: {civciv.isim}, Hayvanın yaşı {civciv.yas}")
