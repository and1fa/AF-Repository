import os
import getpass
import csv

# Data pengguna
user = {"admin": "admin123"}
user_role = {"admin": "admin"}

# Data pasien
data_pasien = []

# Fungsi untuk menyimpan data pasien ke file CSV
def simpan_data():
    with open('datapasien.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Umur", "Alamat", "Nomor Handphone", "Penyakit"])
        for pasien in data_pasien:
            writer.writerow([pasien["Nama"], pasien["Umur"], pasien["Alamat"], pasien["Nomor Handphone"], pasien["Penyakit"]])

# Fungsi untuk memuat data pasien dari file CSV
def muat_data():
    global data_pasien
    if os.path.exists('datapasien.csv'):
        with open('datapasien.csv', 'r') as file:
            reader = csv.DictReader(file)
            data_pasien = [row for row in reader]

# Registrasi pengguna baru
def daftar():
    os.system('cls || clear')
    print("Registrasi Pengguna Baru".center(50))
    print("=" * 50)
    username = input("Masukkan username: ")
    if username in user:
        print("Username sudah ada!")
        input("Klik Enter untuk melanjutkan . . .")
        return
    password = getpass.getpass("Masukkan password: ")
    user[username] = password
    user_role[username] = "pengguna"  # Semua pengguna baru adalah "pengguna"
    print("Registrasi berhasil!")
    print()
    input("Klik Enter untuk melanjutkan . . .")

# Login
def login():
    os.system('cls || clear')
    print("Login".center(50))
    print("=" * 50)
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password (Password akan tertutup): ")
    if user.get(username) == password:
        print("Login berhasil!")
        print()
        input("Enter untuk melanjutkan . . .")
        return username
    else:
        print("Username atau password salah!")
        print()
        input("Enter untuk melanjutkan . . .")
        return None

# Menambahkan data pasien
def buat_data():
    os.system('cls || clear')
    print("Tambah Data Pasien".center(50))
    print("=" * 50)
    nama = input("Nama           : ")
    umur = input("Umur           : ")
    alamat = input("Alamat         : ")
    nomor_hp = input("Nomor Handphone: ")
    penyakit = input("Penyakit       : ")
    data_pasien.append({
        "Nama": nama,
        "Umur": umur,
        "Alamat": alamat,
        "Nomor Handphone": nomor_hp,
        "Penyakit": penyakit
    })
    simpan_data()
    print()
    print("Data berhasil ditambahkan!")
    print()
    input("Klik Enter untuk melanjutkan . . .")

# Menampilkan data pasien
def tampil_data():
    os.system('cls || clear')
    print("Data Pasien Rumah Sakit".center(50))
    print("=" * 50)
    if not data_pasien:
        print("Data belum tersedia.")
        print()
        input("Klik Enter untuk melanjutkan . . .")
        return
    for i, pasien in enumerate(data_pasien, start=1):
        print(f"Pasien {i}:")
        print()
        print(f" Nama           : {pasien['Nama']}")
        print(f" Umur           : {pasien['Umur']}")
        print(f" Alamat         : {pasien['Alamat']}")
        print(f" Nomor Handphone: {pasien['Nomor Handphone']}")
        print(f" Penyakit       : {pasien['Penyakit']}")
        print("=" * 50)
        print()
    input("Klik Enter untuk melanjutkan . . .")

# Memperbarui data pasien
def ubah_data():
    tampil_data()
    print()
    print("Perbarui Data Pasien Rumah Sakit".center(50))
    print("=" * 50)
    if not data_pasien:
        return
    try:
        index = int(input("Masukkan nomor pasien yang akan diperbarui: ")) - 1
        if 0 <= index < len(data_pasien):
            nama = input("Nama           : ")
            umur = input("Umur           : ")
            alamat = input("Alamat         : ")
            nomor_hp = input("Nomor Handphone: ")
            penyakit = input("Penyakit       : ")
            data_pasien[index] = {
                "Nama": nama,
                "Umur": umur,
                "Alamat": alamat,
                "Nomor Handphone": nomor_hp,
                "Penyakit": penyakit
            }
            simpan_data()
            print("Data berhasil diperbarui!")
            input("Klik Enter untuk melanjutkan . . .")
        else:
            print("Nomor pasien tidak valid!")
            input("Klik Enter untuk melanjutkan . . .")
    except ValueError:
        print("Input tidak valid!")
        input("Klik Enter untuk melanjutkan . . .")

# Menghapus data pasien
def hapus_data():
    tampil_data()
    print()
    print("Hapus Data Pasien Rumah Sakit".center(50))
    print("=" * 50)
    if not data_pasien:
        return
    try:
        index = int(input("Masukkan nomor pasien yang akan dihapus: ")) - 1
        if 0 <= index < len(data_pasien):
            data_pasien.pop(index)
            simpan_data()
            print()
            print("Data berhasil dihapus!")
            print()
            input("Klik Enter untuk melanjutkan . . .")
        else:
            print("Nomor pasien tidak valid!")
            print()
            input("Klik Enter untuk melanjutkan . . .")
    except ValueError:
        print("Input tidak valid!")
        tampil_data()

# Menu utama
def main():
    muat_data()
    while True:
        os.system('cls || clear')
        print("=" * 50)
        print("Sistem Manajemen Data Pasien Rumah Sakit".center(50))
        print("=" * 50)
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        print("=" * 50)
        pilihan = input("Pilih opsi: ").strip()
        if pilihan == "1":
            username = login()
            if username:
                while True:
                    os.system('cls || clear')
                    print("=" * 50)
                    print("Sistem Manajemen Data Pasien Rumah Sakit".center(50))
                    print("=" * 50)
                    print(f"Selamat Datang {username}, Silakan pilih menu")
                    print()
                    print("1. Tambah Data Pasien")
                    print("2. Lihat Data Pasien")
                    print("3. Perbarui Data Pasien")
                    print("4. Hapus Data Pasien")
                    print("5. Logout")
                    print("=" * 50)
                    pilihan = input("Masukkan opsi: ").strip()
                    if pilihan == "1":
                        if user_role[username] == "admin":
                            buat_data()
                        else:
                            print("Hanya admin yang dapat menambah data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "2":
                        tampil_data()
                    elif pilihan == "3":
                        if user_role[username] == "admin":
                            ubah_data()
                        else:
                            print("Hanya admin yang dapat memperbarui data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "4":
                        if user_role[username] == "admin":
                            hapus_data()
                        else:
                            print("Hanya admin yang dapat menghapus data!")
                            print()
                            input("Klik Enter untuk melanjutkan . . .")
                    elif pilihan == "5":
                        break
                    else:
                        print("Opsi tidak valid!")
                        input("Klik Enter untuk melanjutkan . . .")
        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            break
        else:
            print("Opsi tidak valid!")
            input("Klik Enter untuk melanjutkan . . .")

if __name__ == "__main__":
    main()
