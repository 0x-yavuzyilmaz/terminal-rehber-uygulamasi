import time


def yavas_islem():
    print("Yavaş işlem başlıyor...")
    time.sleep(2)  # Programı 2 saniye bekletir.
    print("Yavaş işlem bitti.")




def zaman_olcer_decorator(suslenecek_fonksiyon):
    def sarmalayici_fonksiyon():
        baslangic_zamani = time.time()

        suslenecek_fonksiyon()

        bitis_zamani = time.time()
        gecen_sure = bitis_zamani - baslangic_zamani
        print(f"--- '{suslenecek_fonksiyon.__name__}' fonksiyonu {gecen_sure:.2f} saniye sürdü. ---")

    return sarmalayici_fonksiyon


@zaman_olcer_decorator
def hizli_islem():
    print("Hızlı işlem başlıyor...")
    time.sleep(0.5)  # Programı 0.5 saniye bekletir.
    print("Hızlı işlem bitti.")

hizli_islem()