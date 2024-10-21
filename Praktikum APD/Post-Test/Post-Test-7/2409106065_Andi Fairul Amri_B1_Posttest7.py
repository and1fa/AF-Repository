import os
import getpass

# Data pengguna
user = {"admin": "admin123"}  # Akun untuk admin
user_role = {"admin": "admin"}

# Data penghuni asrama
penghuni_asrama = {}

# Registrasi pengguna baru
def daftar():
    os.system('cls || clear')
    print("Registrasi Pengguna Baru".center(50))
    print("=" * 50)
    username = input("Masukkan username: ")
    if username in user:
        print("Username sudah ada!")
        input("Klik Enter untuk melanjutkan . . .")
        return False  # Registrasi gagal
    password = getpass.getpass("Masukkan password: ")
    user[username] = password
    user_role[username] = "pengguna"  # Semua pengguna baru adalah "pengguna"
    print("Registrasi berhasil!")
    print()
    input("Klik Enter untuk melanjutkan . . .")
    return True  # Registrasi berhasil

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

# Menambahkan data penghuni
def buat_data():
    os.system('cls || clear')
    print("Tambah Data Penghuni".center(50))
    print("=" * 50)
    nama = input("Nama           : ")
    universitas = input("Universitas    : ")
    tahun_masuk = input("Tahun Masuk    : ")
    nomor_hp = input("Nomor Handphone: ")
    nomor_kamar = input("Nomor Kamar    : ")
    penghuni_asrama[nama] = {
        "universitas": universitas,
        "tahun_masuk": tahun_masuk,
        "nomor_hp": nomor_hp,
        "nomor_kamar": nomor_kamar
    }
    print()
    print("Data berhasil ditambahkan!")
    print()
    input("Klik Enter untuk melanjutkan . . .")

# Menghitung jumlah penghuni
def hitung_penghuni(penghuni):
    return len(penghuni)

# Fungsi menampilkan data penghuni
def tampilkan_penghuni(penghuni, index=0):
    if index < len(penghuni):
        nama = list(penghuni.keys())[index]
        data = penghuni[nama]
        print(f"Penghuni {index + 1}:")
        print(f" Nama           : {nama}")
        print(f" Universitas    : {data['universitas']}")
        print(f" Tahun Masuk    : {data['tahun_masuk']}")
        print(f" Nomor Handphone: {data['nomor_hp']}")
        print(f" Nomor Kamar    : {data['nomor_kamar']}")
        print("=" * 50)
        tampilkan_penghuni(penghuni, index + 1)

# Menampilkan data penghuni
def tampil_data():
    os.system('cls || clear')
    print("Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        print("Data belum tersedia.")
        print()
        input("Klik Enter untuk melanjutkan . . .")
        return
    print(f"Jumlah Penghuni: {hitung_penghuni(penghuni_asrama)}")  # Memanggil fungsi hitung_penghuni
    print("=" * 50)
    tampilkan_penghuni(penghuni_asrama)
    input("Klik Enter untuk melanjutkan . . .")

# Memperbarui data penghuni
def ubah_data():
    tampil_data()
    print()
    print("Perbarui Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        return
    nama_lama = input("Masukkan nama penghuni yang akan diperbarui: ")
    if nama_lama in penghuni_asrama:
        nama_baru = input("Nama Baru      : ")
        universitas = input("Universitas    : ")
        tahun_masuk = input("Tahun Masuk    : ")
        nomor_hp = input("Nomor Handphone: ")
        nomor_kamar = input("Nomor Kamar    : ")
        penghuni_asrama[nama_baru] = {
            "universitas": universitas,
            "tahun_masuk": tahun_masuk,
            "nomor_hp": nomor_hp,
            "nomor_kamar": nomor_kamar
        }
        if nama_baru != nama_lama:
            del penghuni_asrama[nama_lama]
        print("Data berhasil diperbarui!")
        input("Klik Enter untuk melanjutkan . . .")
    else:
        print("Nama penghuni tidak valid!")
        input("Klik Enter untuk melanjutkan . . .")

# Menghapus data penghuni
def hapus_data():
    tampil_data()
    print()
    print("Hapus Data Penghuni Asrama".center(50))
    print("=" * 50)
    if not penghuni_asrama:
        return
    nama = input("Masukkan nama penghuni yang akan dihapus: ")
    if nama in penghuni_asrama:
        del penghuni_asrama[nama]
        print()
        print("Data berhasil dihapus!")
        print()
        input("Klik Enter untuk melanjutkan . . .")
    else:
        print("Nama penghuni tidak valid!")
        print()
        input("Klik Enter untuk melanjutkan . . .")

# Menu Utama
def menu_utama(username):
    while True:
        os.system('cls || clear')
        print("=" * 50)
        print("Sistem Manajemen Data Penghuni Asrama".center(50))
        print("=" * 50)
        print(f"Selamat Datang {username}, Silakan pilih menu")
        print()
        print("1. Tambah Data Penghuni")
        print("2. Lihat Data Penghuni")
        print("3. Perbarui Data Penghuni")
        print("4. Hapus Data Penghuni")
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

# Autentikasi
def main():
    while True:
        print("Selamat Datang di Sistem Manajemen Data Penghuni Asrama!")
        os.system('cls || clear')
        print("=" * 50)
        print("Sistem Manajemen Data Penghuni Asrama".center(50))
        print("=" * 50)
        print("1. Login")
        print("2. Daftar")
        print("3. Keluar")
        print("=" * 50) 
        pilihan = input("Pilih opsi: ").strip()
        if pilihan == "1":
            username = login()
            if username:
                menu_utama(username)  
        elif pilihan == "2":
            daftar()
        elif pilihan == "3":
            break
        else:
            print("Opsi tidak valid!")
            input("Klik Enter untuk melanjutkan . . .")

if __name__ == "__main__":
    main()