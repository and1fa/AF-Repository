# Program Menghitung Luas atau Keliling Bangun Datar dengan Menu Pilihan

# Import os untuk menggunakan cls
import os

# Menampilkan menu yang tersedia
print("=" *70)
print("Program Menghitung Luas/Keliling Bangun Datar" .center(70))
print("=" *70)
print("""Pilihan Menu :
      1. Luas Persegi Panjang 
      2. Keliling Persegi Panjang 
      3. Luas Persegi 
      4. Keiling Persegi 
      5. Keluar Program """)
print("=" *70)

# Input menu yang diinginkan
menu = int(input("Masukkan pilihan menu anda : "))

# Membersihkan terminal
os.system('cls')

# Jika memilih menu 1   
if menu == 1:
    print("=" *70)
    print("Program Menghitung Luas Persegi Panjang".center(70))
    print("=" *70)
    p = float(input("Masukkan Panjang (cm) : "))
    l = float(input("Masukkan Lebar (cm) : "))
    hasil = p*l
    print(f"Luas Persegi Panjang adalah {hasil:.1f} cm²")

# Jika memilih menu 2
elif menu == 2:
    print("=" *70)
    print("Program Menghitung Keliling Persegi Panjang".center(70))
    print("=" *70)
    p = float(input("Masukkan Panjang (cm) : "))
    l = float(input("Masukkan Lebar (cm) : "))
    hasil = p+p+l+l
    print(f"Keliling Persegi Panjang adalah {hasil:.1f}")

# Jika memilih menu 3
elif menu == 3:
    print("=" *70)
    print("Program Menghitung Luas Persegi".center(70))
    print("=" *70)
    s = float(input("Masukkan Sisi (cm) : "))
    hasil = s*s
    print(f"Luas Persegi adalah {hasil:.1f} cm²")

# Jika memilih menu 4
elif menu == 4:
    print("=" *70)
    print("Program Menghitung Keliling Persegi".center(70))
    print("=" *70)
    s = float(input("Masukkan Sisi (cm) : "))
    hasil = s*4
    print(f"Keliling Persegi adalah {hasil:.1f} cm")

# Jika memilih menu 5
elif menu == 5:
    print("Anda keluar dari program")

# Jika memilih menu yang tidak ada
else:
    print("Pilihan tidak ada")
