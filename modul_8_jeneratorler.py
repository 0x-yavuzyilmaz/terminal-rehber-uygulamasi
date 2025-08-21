
buyuk_liste = [i**3 for i in range(1,1_000_001)]
print(buyuk_liste)

print(f" Listenin tipi: {type(buyuk_liste)}")

tembel_jenerator = (i**3 for i in range(1,1_000_001))
print(tembel_jenerator)

print(f" Listenin tipi: {type(tembel_jenerator)}")

print("\n Jeneratörden ilk 5 eleman isteniyor: ")
sayac = 0

for kup in tembel_jenerator:
    print(kup)
    sayac = sayac + 1
    if sayac == 5:
        break

# ("Eğer bir sonraki projemde çok büyük bir log dosyasını satır satır işleyecek olsam,"
# " tüm satırları önce bir listeye mi okurdum, yoksa satırları bir jeneratör gibi mi ele alırdım? Neden?")

# çok büyük bir log satırını satır satır işlşeyecek olsam.Tüm satırları bir listeye okumazdım.çünkü tüm satırların
# listede bellekte olmasına gerek yok gereksiz bellek israfı oluşturur. onun yerine generatör kullanmak çok daha
# not verimlidir. ancak tabi sonrasında bir kaç blok daha kod yazmak gerekiyor:)