"""

# 'w' modu: "write" (yazma) anlamına gelir.
# DİKKAT: Eğer 'notlarim.txt' adında bir dosya zaten varsa, 'w' modu
# içindeki her şeyi SİLER ve üzerine yazar. Sıfırdan yazar.
with open('notlarim.txt', 'w') as dosya:
    dosya.write("Bu benim ilk kalıcı notum.\n")
    dosya.write("Dosya işlemleri harika!\n")
    dosya.write("Üçüncü satır.")

print("'notlarim.txt' dosyası başarıyla oluşturuldu ve yazıldı.")
"""

with open("notlarim.txt", "w") as dosya:
    dosya.write("Bu benim ilk kalıcı notum.\n")
    dosya.write("Dosya işlemleri harika!\n")
    dosya.write("3. satır yazıldı.")

print(" \"notlarim.txt\" dosyası başarıyla olulşturuldu ve yazıldı. ")