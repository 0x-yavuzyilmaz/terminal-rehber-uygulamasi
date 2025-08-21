# --- YAZMA AŞAMASI (Değişiklik yok, burası mükemmeldi) ---
skorlar = [
    {'oyuncu': 'WALTER', 'skor': 1200},
    {'oyuncu': 'JESSE', 'skor': 950},
    {'oyuncu': 'SAUL', 'skor': 1500},
    # Bozuk verileri test etmek için ekleyelim:
    # {'oyuncu': 'FLYNN', 'skor': 'BESYUZ'}, # Bu ValueError'a neden olacak
    # {'oyuncu': 'MIKE'}, # Bu KeyError'a neden olurdu (daha ileri bir konu)
]

try:
    with open('skor_kaydi.txt', 'w') as dosya:
        for nesne in skorlar:
            dosya.write(f"{nesne['oyuncu']},{nesne['skor']}\n")
    print('Skor tablosu başarıyla dosyaya yazıldı.')

except Exception as e:  # Genel bir hata yakalama (daha sonra göreceğiz)
    print(f"Yazma sırasında bir hata oluştu: {e}")

# --- OKUMA AŞAMASI (Cilalanmış hali) ---
geri_yuklenen_skorlar = []
try:
    with open('skor_kaydi.txt', 'r') as dosya:
        for satir in dosya:
            try:
                temiz_satir = satir.strip()
                parcalar = temiz_satir.split(',')

                oyuncu_adi = parcalar[0]
                skor_miktari = int(parcalar[1])

                yeni_sozluk = {"oyuncu": oyuncu_adi, "skor": skor_miktari}
                geri_yuklenen_skorlar.append(yeni_sozluk)

            except (ValueError, IndexError):  # İKİ HATA TÜRÜ BİRLEŞTİRİLDİ
                print(f"Uyarı: '{temiz_satir}' formatındaki bozuk satır atlandı.")

    print("\n--- Başarıyla Okunan Skorlar ---")
    print(geri_yuklenen_skorlar)

except FileNotFoundError:
    print("Hata: Skor dosyası bulunamadı. Henüz hiç skor kaydedilmemiş olabilir.")
