import datetime 

print("\n"+5*"="+" PROGRAM PENGHITUNG UMUR "+"="*5+"\n")

print(f"Masukkan Tanggal, Bulan, dan Tahun Lahir anda\n")
Tanggal = int(input("Tanggal\t: ")) #Input Umur User
Bulan = int(input("Bulan\t: "))
Tahun = int(input("Tahun\t: "))

umur_user = datetime.date(Tahun,Bulan,Tanggal) # Format YY/MM/DD
print(f"\nTanggal lahir anda adalah: {umur_user} pada hari {umur_user:%A}") # %A akan mengubah datetime.date ke hari

hari_ini = datetime.date.today() # %A akan mengubah datetime.date ke hari
print(f"Hari ini adalah {hari_ini:%A} {hari_ini}")

umur_hari = hari_ini - umur_user
umur_tahun = umur_hari.days // 365
umur_bulan = (umur_hari.days % 365) // 30 

ultah_depan = datetime.date((hari_ini.year), Bulan, Tanggal)

if ultah_depan < hari_ini:
    ultah_depan = datetime.date((hari_ini.year +1), Bulan, Tanggal)

day_to_bday = ultah_depan - hari_ini

if ultah_depan == hari_ini:
    ultah_depan = datetime.date((hari_ini.year +1), Bulan, Tanggal)
    day_to_bday = ultah_depan - hari_ini

print(f"Umur anda adalah {umur_tahun} tahun, {umur_bulan} bulan")
print(f"Dan anda akan ultah {day_to_bday.days} Hari lagi")
