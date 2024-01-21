# Program Konversi Suhu Sederhana dari Celcius ke Suhu lainnya

print("\n" + 5*"=" + " Program Konversi Suhu Celcius " + "="*5)
celcius = float(input("\nMasukkan Suhu Celcius: "))

# Reamur
reamur = (4/5) * celcius
print("\nSuhu dalam Reamur adalah:",reamur, "Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah:",fahrenheit, "fahrenheit")

# Kelvin
kelvin = celcius + 273
print("Suhu dalam Kelvin adalah:",kelvin, "Kelvin")
print("\n" + 5*"=" + " Akhir dari Program " + "="*5)
