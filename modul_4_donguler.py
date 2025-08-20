yapilacaklar = ["kirayı öde", "projeyi bitir", "spor yap"]

print("--- Görev Listesi ---")
for gorev in yapilacaklar:
    # Bu girintili blok, döngünün her adımında tekrar tekrar çalışır
    print(f"- {gorev.title()}") # .title() metodu string'in baş harflerini büyütür

print("--- Liste Bitti ---")