rakamlar = []
print("Döngü başlıyor...")

for i in range(5):
    yeni_rakam = i * 2
    rakamlar.append(yeni_rakam)
    print(f"Adım {i+1}: Liste = {rakamlar}")

print("Döngü bitti!")
print(f"Listenin son hali: {rakamlar}")