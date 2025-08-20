kelimeler = ["Elma", "armut", "Muz", "Kiraz", "Karpuz", "Ayva", "nar", "Ejder Meyvesi", "Ananas"]

uzun_kelimeler_dongu = []

for kelime in kelimeler:
    if len(kelime) > 5:
        uzun_kelimeler_dongu.append(kelime)

print(uzun_kelimeler_dongu)

uzun_kelimeler_comp = [kelime for kelime in kelimeler if len(kelime) > 5]

print(uzun_kelimeler_comp)

a_ile_baslayan_buyuk_harf = [kelime.upper() for kelime in kelimeler if kelime.lower().startswith("a")]

print(a_ile_baslayan_buyuk_harf)