yapilacaklar = ["pazara git", "faturayı öde", "projeyi bitir"]
print(yapilacaklar)

yapilacaklar.append("spor yap")
print(yapilacaklar[1])

yapilacaklar[1] = "kirayı öde"
yapilacaklar.remove("pazara git")
print(f"Listenin Son Hali: {yapilacaklar}")
