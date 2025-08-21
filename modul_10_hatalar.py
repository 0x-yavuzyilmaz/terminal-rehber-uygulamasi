yas_str = input("Yaşınızı giriniz: ")
yas_int = int(yas_str) # Kullanıcı "yirmi" gibi bir şey yazarsa ne olur?
print(f"İki yıl sonra {yas_int + 2} yaşında olacaksınız.")

# İYİ KOD (Sağlam)
# try:
#     yas_str = input("Yaşınızı giriniz: ")
#     yas_int = int(yas_str) # Tehlikeli operasyon burada
#     print(f"İki yıl sonra {yas_int + 2} yaşında olacaksınız.")
# except ValueError:
#     # Eğer int() fonksiyonu bir string'i sayıya çeviremezse ValueError hatası verir.
#     print("Hata: Lütfen yaşınızı bir sayı olarak giriniz.")
#
# print("Program normal bir şekilde sona erdi.")