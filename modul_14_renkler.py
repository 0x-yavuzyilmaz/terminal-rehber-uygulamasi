from colorama import Fore, Style, init

# Colorama'yı terminalde çalışması için başlat
init(autoreset=True)

print("Bu normal bir yazı.")
print(Fore.RED + "Bu kırmızı bir yazı.")
print(Fore.GREEN + Style.BRIGHT + "Bu yeşil bir yazı.")
print(Fore.YELLOW + Style.BRIGHT + "Bu parlak sarı bir yazı.")
# Style.RESET_ALL'a gerek yok çünkü autoreset=True