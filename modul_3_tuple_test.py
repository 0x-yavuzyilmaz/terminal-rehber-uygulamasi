# Bir liste (değiştirilebilir)
bir_nokta_liste = [10, 20]
bir_nokta_liste[0] = 15 # Sorun yok
print(f"Liste: {bir_nokta_liste}")

# Bir tuple (değiştirilemez)
bir_nokta_tuple = (10, 20)
print(f"Tuple: {bir_nokta_tuple}")

# Şimdi tuple'ı değiştirmeye çalışalım
print("Tuple'ı değiştirmeye çalışıyorum...")
bir_nokta_tuple[0] = 15 # BU SATIR HATA VERECEK!