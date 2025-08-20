def vki_hesapla(kilo_kg, boy_m):
    return kilo_kg / (boy_m * boy_m)

weight= float(input("Lütfen Ağırlığınızı Giriniz: "))
length = float(input("Lütfen Boyunuzu Giriniz: "))

kullanici_vki = vki_hesapla(weight, length)

print(f"Vücut Kitle endeksiniz: {kullanici_vki:.2f}")
