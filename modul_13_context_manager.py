import time


class ZamanOlcer:
    def __init__(self):
        pass

    def __enter__(self):
        print("-> Zaman ölçümü başladı.")
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        gecen_zaman = self.end_time - self.start_time
        print(f"<- Zaman ölçümü bitti. Geçen süre: {gecen_zaman:.4f} saniye")


with ZamanOlcer():
    # İçine, zamanını ölçmek istediğimiz bir işlem koyalım.
    print("   ... Uzun bir işlem yapılıyor ...")
    time.sleep(1.5)  # Programı 1.5 saniye uyut.
