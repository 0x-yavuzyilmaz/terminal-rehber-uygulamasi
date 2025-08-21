from datetime import datetime

# O anın tam tarihini ve saatini alıp güzel bir string formatına çevirir

# Çıktı şuna benzer: "2024-05-25 14:30:55"


try:
    print("--- Önceki Günlük Girdileri ---")
    with open('gunluk.txt', 'r') as dosya:
        icerik = dosya.read()
        if icerik:
            print(icerik)
        else:
            print("Henüz günlük oluşturulmamış.")

except FileNotFoundError:
    print("Günlük dosyanız oluşturulmamış. İlk girdiniz oluşturulacak.")


yeni_girdi = input("Bugün Ne düşünüyorsun?\n")

with open('gunluk.txt', 'a') as dosya:
    zaman_damgasi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dosya.write(f"[{zaman_damgasi}] {yeni_girdi}\n")

    print("Girdin başarıyla günlüğe eklendi.")