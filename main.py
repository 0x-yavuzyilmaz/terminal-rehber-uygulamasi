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

# --- ANA PROGRAM AKIŞI ---
rehber = [
    {'isim': 'Walter White', 'telefon': '555-1234'},
    {'isim': 'Jesse Pinkman', 'telefon': '555-5678'},
]

while True:
    print("\n--- Telefon Rehberi ---")
    print("1: Kişileri Göster")
    print("2: Yeni Kişi Ekle")
    print("3: Kişi Sil (Henüz yapılmadı)")
    print("4: Çıkış")

    secim = input("Seçiminiz (1/2/3/4): ")

    if secim == '1':
        kisileri_goster(rehber)
    elif secim == '2':
        kisi_ekle(rehber)
    elif secim == '3':
        print("Bu özellik yakında eklenecek.")
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break  # while döngüsünü kırar ve programı sonlandırır.
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")