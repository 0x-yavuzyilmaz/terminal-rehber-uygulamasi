"""
print("\n'notlarim.txt' dosyasının içeriği okunuyor:")

# 'r' modu: "read" (okuma) anlamına gelir. En yaygın moddur ve belirtmezseniz varsayılan olarak kabul edilir.
try:
    with open('notlarim.txt', 'r') as dosya:
        # 1. Yöntem: Tüm içeriği tek bir string olarak okumak
        # icerik = dosya.read()
        # print("--- read() metodu ---")
        # print(icerik)

        # 2. Yöntem (Genellikle daha kullanışlı): Satır satır okumak
        print("\n--- satır satır okuma ---")
        for satir in dosya:
            print(satir.strip()) # .strip() metodu, satırın başındaki ve sonundaki boşlukları/yeni satır karakterlerini temizler.

except FileNotFoundError:
    print("HATA: 'notlarim.txt' adında bir dosya bulunamadı. Lütfen önce yazma kodunu çalıştırın.")
"""


print("\n'notlarim.txt' dosyasinin içeriği okunuyor.")

try:

    with open('notlarim.txt', 'r') as dosya:
        # icerik = dosya.read()
        # print("--- read() metodu ---")
        # print(icerik)

        for satir in dosya:
            print("\n--- satır satır okuma ---")
            print(satir.strip())

except FileNotFoundError:
    print("HATA: 'notlarim.txt' adında bir dosya bulunamadı. Lütfen önce yazma kodunu çalıştırın.")