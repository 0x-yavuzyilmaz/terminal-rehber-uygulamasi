# --- FONKSİYONLAR ---
def kisileri_goster(rehber_listesi):
    print("--- Rehberdeki Kişiler ---")

    if not rehber_listesi:
        print("Rehberde gösterilecek kimse yok.")
        return

    for kisi_sozlugu in rehber_listesi:
        isim = kisi_sozlugu["isim"]
        telefon = kisi_sozlugu["telefon"]

        print(f"Kişi: {isim} - Telefon: {telefon} ")


def kisi_ekle(rehber_listesi):
    print("--- Yeni Kişi Ekleme ---")

    isim= input("Kişi İsmi Giriniz: ")
    telefon = input("Kişi Telefonu Giriniz:")
    rehber_listesi.append({"isim":isim, "telefon":telefon})

    print(f"{isim} başarı ile rehbere eklendi. ")

def kisi_sil(rehber_listesi):
    print("---Kişi Silme ---")

    silinecek_kisi = input("Lütfen silinecek kişinin adını yazınız:")
    bulunan_kisi = None

    for kisi in rehber_listesi:
        if kisi["isim"].lower() == silinecek_kisi.lower():
            bulunan_kisi = kisi
            break

    if bulunan_kisi:
        rehber_listesi.remove(bulunan_kisi)
        print(f"{bulunan_kisi["isim"]} listeden başarı ile silindi.")
    else:
        print(f"{silinecek_kisi} bulunamadı.")


def kisi_guncelle(rehber_listesi):
    print("--- Rehberdeki Kişileri Günceller ---")
    guncellenecek_kisi = input("Lütfen güncellencek kişinin adını yazınız:")


    for kisi in rehber_listesi:
        if kisi["isim"].lower() == guncellenecek_kisi.lower():
            yeni_telefon = input("Lütfen yeni numarayı yazınız:")
            kisi["telefon"] = yeni_telefon
            print("Güncelleme Başarılı!")
            break
        else:
            print("Kişi Bulunamadı!")





# --- ANA PROGRAM AKIŞI ---
rehber = [
    {'isim': 'Walter White', 'telefon': '555-1234'},
    {'isim': 'Jesse Pinkman', 'telefon': '555-5678'},
]




while True:
    print("\n--- Telefon Rehberi ---")
    print("1: Kişileri Göster")
    print("2: Yeni Kişi Ekle")
    print("3: Kişi Sil")
    print("4: Kişi Güncelle")
    print("5: Çıkış")

    secim = input("Seçiminiz (1/2/3/4/5): ")

    if secim == '1':
        kisileri_goster(rehber)
    elif secim == '2':
        kisi_ekle(rehber)
    elif secim == '3':
        kisi_sil(rehber)
    elif secim == '4':
        kisi_guncelle(rehber)
    elif secim == '5':
        print("Programdan çıkılıyor...")
        break  # while döngüsünü kırar ve programı sonlandırır.
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")