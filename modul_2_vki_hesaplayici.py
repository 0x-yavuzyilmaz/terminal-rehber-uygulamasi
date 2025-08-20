weight_kg_input = input("Lütfen ağırlığını giriniz: ")
length_meters_input = input("Lütfen boyunuzu giriniz: ")

weight_kgs = float(weight_kg_input)
length_meters = float(length_meters_input)

bmi = weight_kgs / (length_meters * length_meters)

print(f" Vücut kitle endeksiniz: {bmi:.2f}")
