# Program untuk membuat biodata menggunakan fungsi input()

# Input data
nama = input("Masukkan Nama: ")
umur = int(input("Masukkan Umur (tahun): "))
tinggi_badan = float(input("Masukkan Tinggi Badan (cm): "))
menikah = bool(input("Apakah sudah menikah (ya/tidak): ").lower()) == 'ya'

# Menghitung total dari variabel bertipe int dan float
total = umur + tinggi_badan

# Mencetak biodata
print("=" *40)
print("Biodata Anda".center(40))
print("=" *40)
print(f"Nama                 : {nama}")
print(f"Umur                 : {umur} Tahun")
print(f"Tinggi Badan         : {tinggi_badan:.1f} cm")
print(f"Status Pernikahan    : {'Sudah Menikah' if menikah else 'Belum Menikah'}")
print("=" *40)
print(f"Total (Umur + Tinggi Badan): {total}")
print("=" *40)