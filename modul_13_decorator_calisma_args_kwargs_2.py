"""
Bir önceki alıştırmada yazdığın selamla_decorator'ı al.

Adını evrensel_selamla_decorator olarak değiştir.
sarmalayici_fonksiyon'u *args ve **kwargs kabul edecek şekilde güncelle.
suslenecek_fonksiyon'u çağırırken, bu *args ve **kwargs'ı ona aynen aktar.
Bu yeni ve güçlü decorator'ı test etmek için iki yeni fonksiyon yaz:
ad_soyad_yaz(ad, soyad) adında, iki konumsal argüman alan bir fonksiyon.
bilgileri_isle(kullanici_id, durum='aktif') adında, hem konumsal hem de anahtar kelimeli argüman alan bir fonksiyon.
Bu iki yeni fonksiyonu da @evrensel_selamla_decorator ile süsle ve çalıştırarak test et.
"""


def evrensel_selamla_decorator(suslenecek_fonksiyon):
    def sarmalayici_fonksiyon(*args, **kwargs):
        print("Merhaba! Fonksiyon çalışmak üzere.")
        suslenecek_fonksiyon(*args, **kwargs)
        print("Hoşça kal! Fonksiyon işini bitirdi.")

    return sarmalayici_fonksiyon


@evrensel_selamla_decorator
def ad_soyad_yaz(ad, soyad):
    print(f"Kişinin adı: {ad} Kişinin soyadı: {soyad}")


@evrensel_selamla_decorator
def bilgilerini_isle(kullanici_id, durum="bilinmiyor"):
    print(f"Kişinin kullanıcı adı: {kullanici_id}, DURUM: {durum} ")


ad_soyad_yaz(ad="Yavuz", soyad="YILMAZ")
print("-" * 20)

bilgilerini_isle("Jafus","Aktif")
print("-" * 20)

bilgilerini_isle("admin")