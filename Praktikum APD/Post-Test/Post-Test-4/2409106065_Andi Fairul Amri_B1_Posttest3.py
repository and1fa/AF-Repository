# Import os untuk menggunakan cls
import os

# Autentikasi
print("=" *70)
print("Selamat Datang di Program Ini" .center(70))
print("=" *70)
print("Silakan login terlebih dahulu")
kesempatan = 3


while kesempatan >0:
    masukan_username = input("Masukkan username: ")
    masukan_password = input("Masukkan password: ")
    if masukan_username == "afa" and masukan_password == "065":
        print("Login berhasil")
        os.system('cls')
        break
    else:
        print("Username atau password salah, silahkan coba lagi")
        print(f"kesempatan mencoba tersisa {kesempatan} kali")
else:
    print("Terlalu banyak percobaan yang gagal. Program keluar.")
    exit()


# Program Menghitung Luas atau Keliling Bangun Datar dengan Menu Pilihan

# Menampilkan menu yang tersedia
while True:
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
        panjang = float(input("Masukkan Panjang (cm) : "))
        lebar = float(input("Masukkan Lebar (cm) : "))
        hasil = panjang*lebar
        print(f"Luas Persegi Panjang adalah {hasil:.1f} cm²")
       
    # Jika memilih menu 2
    elif menu == 2:
        print("=" *70)
        print("Program Menghitung Keliling Persegi Panjang".center(70))
        print("=" *70)
        panjang = float(input("Masukkan Panjang (cm) : "))
        lebar = float(input("Masukkan Lebar (cm) : "))
        hasil = panjang+panjang+lebar+lebar
        print(f"Keliling Persegi Panjang adalah {hasil:.1f}")

    # Jika memilih menu 3
    elif menu == 3:
        print("=" *70)
        print("Program Menghitung Luas Persegi".center(70))
        print("=" *70)
        sisi = float(input("Masukkan Sisi (cm) : "))
        hasil = sisi*sisi
        print(f"Luas Persegi adalah {hasil:.1f} cm²")

    # Jika memilih menu 4
    elif menu == 4:
        print("=" *70)
        print("Program Menghitung Keliling Persegi".center(70))
        print("=" *70)
        sisi = float(input("Masukkan Sisi (cm) : "))
        hasil = sisi*4
        print(f"Keliling Persegi adalah {hasil:.1f} cm")

    # Jika memilih menu 5
    elif menu == 5:
        print("Anda keluar dari program, Terima kasih")
        break

    # Jika memilih menu yang tidak ada
    else:
        print("Pilihan tidak ada, silakan coba lagi")


        
