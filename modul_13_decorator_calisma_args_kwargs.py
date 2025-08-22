"""
def hepsini_topla(*sayilar):
    print(f"Gelen sayılar (bir tuple): {sayilar}")
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

print(hepsini_topla(1, 2, 3))       # Çıktı: 6
print(hepsini_topla(10, 20, 30, 40)) # Çıktı: 100
print(hepsini_topla(5))             # Çıktı: 5

def kullanici_profili_yazdir(**bilgiler):
    print(f"Gelen bilgiler (bir sözlük): {bilgiler}")
    for anahtar, deger in bilgiler.items():
        print(f"- {anahtar.title()}: {deger}")

kullanici_profili_yazdir(isim="Walter", yas=52, meslek="Kimya Öğretmeni")
print("-" * 20)
kullanici_profili_yazdir(kullanici_adi="Jesse", sehir="Albuquerque", durum="Karmaşık")
"""

import time
def evrensel_zaman_olcer(suslenecek_fonksiyon):
    def sarmalayici_fonksiyon(*args, **kwargs):
        print(f"\n--- '{suslenecek_fonksiyon.__name__}' fonksiyonu çalıştırılıyor... ---")
        baslangic_zamani = time.time()
        sonuc = suslenecek_fonksiyon(*args, **kwargs)
        bitis_zamani = time.time()
        gecen_sure = bitis_zamani - baslangic_zamani
        print(f"--- Çalışma süresi: {gecen_sure:.4f} saniye ---")
        return sonuc
    return sarmalayici_fonksiyon



# --- TEST EDELİM ---

@evrensel_zaman_olcer
def selam_ver():
    print("Merhaba Dünya!")


@evrensel_zaman_olcer
def sayilari_topla(a, b, c):
    time.sleep(1)
    return a + b + c


@evrensel_zaman_olcer
def kisi_bilgisi_yaz(isim, sehir="Bilinmiyor"):
    print(f"{isim}, {sehir} şehrinde yaşıyor.")


selam_ver()
toplam = sayilari_topla(10, 20, 30)
print(f"Toplam fonksiyonundan dönen sonuç: {toplam}")
kisi_bilgisi_yaz(isim="Skyler", sehir="Albuquerque")
kisi_bilgisi_yaz(isim="Gus")