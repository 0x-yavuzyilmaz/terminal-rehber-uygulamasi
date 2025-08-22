def selamla_decorator(suslenecek_fonksiyon):
    def sarmalayici_fonksiyon():

        print("Merhaba! Fonksiyon çalışmak üzere.")
        suslenecek_fonksiyon()
        print("Hoşça kal! Fonksiyon işini bitirdi.")

    return sarmalayici_fonksiyon

@selamla_decorator
def gunluk_is():
    print(">>> Günlük işler yapılıyor...")

gunluk_is()

@selamla_decorator
def topla(a, b):
    print(f">>> Sonuç: {a + b}")

topla(5, 3)
