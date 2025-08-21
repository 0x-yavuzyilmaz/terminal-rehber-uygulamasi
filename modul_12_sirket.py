class Calisan:
    def __init__(self, isim: str, soyad: str, maas: int):
        self.isim = isim
        self.soyad = soyad
        self.maas = maas

    def bilgi_ver(self):
        return f"{self.isim} {self.soyad}, Maaş: {self.maas}"


class Yazilimci(Calisan):
    def __init__(self, isim: str, soyad: str, maas: int, bildigi_diller: list):
        super().__init__(isim, soyad, maas)
        self.bildigi_diller = bildigi_diller

    def bilgi_ver(self):
        ebeveynden_gelen_bilgi = super().bilgi_ver()
        return f"{ebeveynden_gelen_bilgi}, Bildiği Diller: {self.bildigi_diller}"


class Yonetici(Calisan):
    def __init__(self, isim: str, soyad: str, maas: int, sorumlu_oldugu_kisi_sayisi: int):
        super().__init__(isim, soyad, maas)
        self.sorumlu_oldugu_kisi_sayisi = sorumlu_oldugu_kisi_sayisi

    def bilgi_ver(self):
        ebeveynden_gelen_bilgi = super().bilgi_ver()
        return f"{ebeveynden_gelen_bilgi}, Sorumlu olduğu kişi sayısı: {self.sorumlu_oldugu_kisi_sayisi}"


ahmet_calisan = Calisan("Ahmet", "Yilmaz", 15000)
print(ahmet_calisan.bilgi_ver())

mehmet_yazilimci = Yazilimci("Mehmet", "Kaya", 20000, ["Java", "Python", "Ruby"])
print(mehmet_yazilimci.bilgi_ver())

selim_yonetici = Yonetici("Selim", "Korkmaz", 30000, 4)
print(selim_yonetici.bilgi_ver())