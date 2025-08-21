class Hesap:
    def __init__(self, hesap_sahibi: str, baslangic_bakiye: float):
        self.sahip = hesap_sahibi
        self.bakiye = baslangic_bakiye
    def bilgiler_goster(self):
        return f" Hesap Sahibi: {self.sahip}, Hesap Bakiyesi: {self.bakiye}"

    def para_yatir(self, miktar: int):
        self.bakiye += miktar
        print(f" Hesaba {miktar} TL yatırıldı. Hesaptaki toplam bakiye: {self.bakiye}")

    def para_cek(self, miktar: int):
        if miktar > self.bakiye:
            print("Yetersiz Bakiye!")
            return
        else:
            self.bakiye -= miktar
            print(f" Hesaptan {miktar} TL çekildi. Hesaptaki toplam bakiye: {self.bakiye}")





hesap_1 = Hesap("Yavuz Yılmaz", 1000)

print(hesap_1.bilgiler_goster())
hesap_1.para_yatir(500)
hesap_1.para_cek(200)
hesap_1.para_cek(2000)

print(hesap_1.bilgiler_goster())
