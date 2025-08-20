# Fonksiyonu burada TANIMLIYORUZ (Defining the function)
# Bu kod henüz ÇALIŞMAZ, sadece Python'a "selam_ver diye bir alet yaptım" deriz.
def selam_ver():
    print("Merhaba, Mimar!")

# Fonksiyonu burada ÇAĞIRIYORUZ (Calling the function)
# Aleti kullanma zamanı. Bu satır, yukarıdaki print komutunu tetikler.
print("Program başlıyor...")
selam_ver()
print("Program bitti.")

# 'isim' burada bir parametredir. Fonksiyonun çalışmak için beklediği bir "girdi".
def isme_gore_selam_ver(isim):
    print(f"Merhaba, {isim}!")

# Şimdi fonksiyonu farklı "argümanlar" ile çağırabiliriz.
isme_gore_selam_ver("Walter")
isme_gore_selam_ver("Jesse")