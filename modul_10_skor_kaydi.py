skorlar = [
    {'oyuncu': 'WALTER', 'skor': 1200},
    {'oyuncu': 'JESSE', 'skor': 950},
    {'oyuncu': 'SAUL', 'skor': 1500}
]

with open('skor_kaydi.txt', 'w') as dosya:
    for nesne in skorlar:
        oyuncu = nesne['oyuncu']
        skor = nesne['skor']
        dosya.write(oyuncu + "," + str(skor) + "\n")

print('Skor tablosu başarıyla dosyaya yazıldı.')


geri_yuklenen_skorlar=[]

with open('skor_kaydi.txt', 'r') as dosya:
    for satir in dosya:
        nesne = satir.strip()

        parcalar= nesne.split(',')

        oyuncu_adi = parcalar[0]
        skor_miktari = int(parcalar[1])

        yeni_sozluk = {"oyuncu":oyuncu_adi, "skor": skor_miktari}
        geri_yuklenen_skorlar.append(yeni_sozluk)



print(geri_yuklenen_skorlar)
