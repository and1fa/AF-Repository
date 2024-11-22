import json
import os
from tabulate import tabulate

data_akun = "data_akun.json"
data_pasien = "data_pasien.json"

# Fungsi untuk membaca data dari file JSON
def muat_data(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Fungsi untuk validasi input (memastikan input tidak kosong)
def valid_input(prompt):
    user_input = input(prompt).strip()
    while not user_input:
        print("Input tidak boleh kosong!")
        user_input = input(prompt).strip()
    return user_input

# Fungsi untuk validasi password
def valid_password(password):
    return len(password) >= 8

# Fungsi untuk membersihkan layar
def clear_screen():
    os.system('cls || clear')

# Fungsi untuk menampilkan data dalam bentuk tabel
def tampilkan_tabel(data, headers):
    print(tabulate(data, headers=headers, tablefmt="heavy_grid"))

# Fungsi untuk menu admin
def menu_admin(data_akun, data_pasien):
    while True:
        clear_screen()
        print("=== Menu Admin ===")
        print("1. Lihat Data Akun Dokter")
        print("2. Tambah Akun Dokter")
        print("3. Edit Akun Dokter")
        print("4. Hapus Akun Dokter")
        print("5. Lihat Data Guest")
        print("6. Hapus Akun Guest")
        print("7. Logout")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            # Tampilkan tabel akun dokter
            dokter_data = [akun for akun in data_akun if akun['role'] == 'dokter']
            dokter_tabel = [[akun['id'], akun['username'], akun['nama'], akun['spesialis'], akun['ruangan']] for akun in dokter_data]
            tampilkan_tabel(dokter_tabel, ["ID Dokter", "Username", "Nama", "Spesialis", "Ruangan"])
            input("Tekan enter untuk kembali...")
        elif pilih == '2':
            # Tambah akun dokter
            id_baru = f"DKT{len(data_akun) + 1:03d}"
            while True:
                username = valid_input("Username: ")
                # Cek apakah username sudah ada
                if any(akun['username'] == username for akun in data_akun):
                    print("Username telah terpakai. Silakan pilih username lain.")
                else:
                    break  # Username valid, keluar dari loop
            password = valid_input("Password: ")
            while not valid_password(password):
                print("Password harus minimal 8 karakter!")
                password = valid_input("Password: ")
            nama = valid_input("Nama Dokter: ")
            spesialis = valid_input("Spesialis: ")
            ruangan = valid_input("Ruangan: ")

            dokter_baru = {
                "id": id_baru,
                "username": username,
                "password": password,
                "role": "dokter",
                "nama": nama,
                "spesialis": spesialis,
                "ruangan": ruangan
            }
            data_akun.append(dokter_baru)
            simpan_data("data_akun.json", data_akun)
            print("Akun dokter berhasil ditambahkan!")
            input("Tekan enter untuk kembali...")
        elif pilih == '3':
            # Edit akun dokter
            dokter_data = [akun for akun in data_akun if akun['role'] == 'dokter']
            dokter_tabel = [[akun['id'], akun['username'], akun['nama'], akun['spesialis'], akun['ruangan']] for akun in dokter_data]
            tampilkan_tabel(dokter_tabel, ["ID Dokter", "Username", "Nama", "Spesialis", "Ruangan"])
            id_dokter = valid_input("Masukkan ID Dokter yang ingin diedit (DKTxxx): ").upper()
            dokter = next((akun for akun in data_akun if akun['id'] == id_dokter), None)

            if dokter:
                dokter['username'] = valid_input(f"Username ({dokter['username']}): ") or dokter['username']
                dokter['password'] = valid_input(f"Password ({dokter['password']}): ") or dokter['password']
                dokter['nama'] = valid_input(f"Nama Dokter ({dokter['nama']}): ") or dokter['nama']
                dokter['spesialis'] = valid_input(f"Spesialis ({dokter['spesialis']}): ") or dokter['spesialis']
                dokter['ruangan'] = valid_input(f"Ruangan ({dokter['ruangan']}): ") or dokter['ruangan']
                simpan_data("data_akun.json", data_akun)
                print("Akun dokter berhasil diedit!")
            else:
                print("Dokter tidak ditemukan!")
            input("Tekan enter untuk kembali...")
        elif pilih == '4':
            # Hapus akun dokter
            dokter_data = [akun for akun in data_akun if akun['role'] == 'dokter']
            dokter_tabel = [[akun['id'], akun['username'], akun['nama'], akun['spesialis'], akun['ruangan']] for akun in dokter_data]
            tampilkan_tabel(dokter_tabel, ["ID Dokter", "Username", "Nama", "Spesialis", "Ruangan"])
            id_dokter = valid_input("Masukkan ID Dokter yang ingin dihapus (DKTxxx): ").upper()
            data_akun = [akun for akun in data_akun if akun['id'] != id_dokter]
            simpan_data("data_akun.json", data_akun)
            print("Akun dokter berhasil dihapus!")
            input("Tekan enter untuk kembali...")
        elif pilih == '5':
            # Lihat data guest
            guest_data = [akun for akun in data_akun if akun['role'] == 'guest']
            guest_tabel = [[akun['id'], akun['username'], akun['password']] for akun in guest_data]
            tampilkan_tabel(guest_tabel, ["ID Guest", "Username", "Password"])
            input("Tekan enter untuk kembali...")
        elif pilih == '6':
            # Hapus akun guest
            guest_data = [akun for akun in data_akun if akun['role'] == 'guest']
            guest_tabel = [[akun['id'], akun['username']] for akun in guest_data]
            tampilkan_tabel(guest_tabel, ["ID Guest", "Username"])
            id_guest = valid_input("Masukkan ID Guest yang ingin dihapus (GSTxxx): ").upper()
            data_akun = [akun for akun in data_akun if akun['id'] != id_guest]
            simpan_data("data_akun.json", data_akun)
            print("Akun guest berhasil dihapus!")
            input("Tekan enter untuk kembali...")
        elif pilih == '7':
            break
        else:
            print("Pilihan tidak tersedia.")

# Fungsi untuk menu dokter
def menu_dokter(data_pasien, data_akun, current_user):
    while True:
        clear_screen()
        print("=== Menu Dokter ===")
        print("1. Lihat Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Edit Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Ganti Password")
        print("6. Logout")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            # Tampilkan tabel data pasien lengkap
            pasien_tabel = [
                [pasien['id'], pasien['nama'], pasien['jenis_kelamin'], pasien['golongan_darah'], pasien['berat_badan'], 
                pasien['tinggi_badan'], pasien['diagnosa'], pasien['dokter'], pasien['ruangan']] for pasien in data_pasien
            ]
            tampilkan_tabel(pasien_tabel, ["ID Pasien", "Nama", "Jenis Kelamin", "Golongan Darah", "Berat Badan", "Tinggi Badan", "Diagnosa", "Dokter", "Ruangan"])
            input("Tekan enter untuk kembali...")
        elif pilih == '2':
            # Tambah pasien
            id_baru = f"PSN{len(data_pasien) + 1:03d}"
            nama = valid_input("Nama Pasien: ")
            jenis_kelamin = valid_input("Jenis Kelamin (L/P): ").upper()
            while jenis_kelamin not in ['L', 'P']:
                print("Input tidak valid! Masukkan hanya 'L' untuk Laki-laki atau 'P' untuk Perempuan.")
                jenis_kelamin = valid_input("Jenis Kelamin (L/P): ").upper()
            golongan_darah = valid_input("Golongan Darah: ").upper()
            berat_badan = valid_input("Berat Badan: ")
            tinggi_badan = valid_input("Tinggi Badan: ")
            diagnosa = valid_input("Diagnosa: ")
            dokter = current_user['nama']
            ruangan = current_user['ruangan']

            pasien_baru = {
                "id": id_baru,
                "nama": nama,
                "jenis_kelamin": jenis_kelamin,
                "golongan_darah": golongan_darah,
                "berat_badan": berat_badan,
                "tinggi_badan": tinggi_badan,
                "diagnosa": diagnosa,
                "dokter": dokter,
                "ruangan": ruangan,
            }
            data_pasien.append(pasien_baru)
            simpan_data("data_pasien.json", data_pasien)
            print("Pasien berhasil ditambahkan!")
            input("Tekan enter untuk kembali...")
        elif pilih == '3':
            # Edit pasien
            pasien_tabel = [
                [pasien['id'], pasien['nama'], pasien['jenis_kelamin'], pasien['golongan_darah'], pasien['berat_badan'], 
                pasien['tinggi_badan'], pasien['diagnosa'], pasien['dokter'], pasien['ruangan']] for pasien in data_pasien
            ]
            tampilkan_tabel(pasien_tabel, ["ID Pasien", "Nama", "Jenis Kelamin", "Golongan Darah", "Berat Badan", "Tinggi Badan", "Diagnosa", "Dokter", "Ruangan"])
            id_pasien = valid_input("Masukkan ID Pasien yang ingin diedit (PSNxxx): ").upper()
            pasien = next((p for p in data_pasien if p['id'] == id_pasien), None)

            if pasien:
                # Pastikan pasien yang akan diedit ditangani oleh dokter yang sedang login
                if pasien['dokter'] == current_user['nama']:
                    pasien['nama'] = valid_input(f"Nama Pasien ({pasien['nama']}): ") or pasien['nama']
                    pasien['jenis_kelamin'] = valid_input(f"Jenis Kelamin ({pasien['jenis_kelamin']}): ").upper() or pasien['jenis_kelamin']
                    while pasien['jenis_kelamin'] not in ['L', 'P']:
                        print("Input tidak valid! Masukkan hanya 'L' untuk Laki-laki atau 'P' untuk Perempuan.")
                        pasien['jenis_kelamin'] = valid_input("Jenis Kelamin (L/P): ").upper()
                    pasien['golongan_darah'] = valid_input(f"Golongan Darah ({pasien['golongan_darah']}): ").upper() or pasien['golongan_darah']
                    pasien['berat_badan'] = valid_input(f"Berat Badan ({pasien['berat_badan']}): ") or pasien['berat_badan']
                    pasien['tinggi_badan'] = valid_input(f"Tinggi Badan ({pasien['tinggi_badan']}): ") or pasien['tinggi_badan']
                    pasien['diagnosa'] = valid_input(f"Diagnosa ({pasien['diagnosa']}): ") or pasien['diagnosa']
                    simpan_data("data_pasien.json", data_pasien)
                    print("Data pasien berhasil diedit!")
                else:
                    print("Anda tidak memiliki izin untuk mengedit data pasien ini.")
            else:
                print("Pasien tidak ditemukan!")
            input("Tekan enter untuk kembali...")
        elif pilih == '4':
            # Hapus pasien
            pasien_tabel = [
                [pasien['id'], pasien['nama'], pasien['jenis_kelamin'], pasien['golongan_darah'], pasien['berat_badan'], 
                pasien['tinggi_badan'], pasien['diagnosa'], pasien['dokter'], pasien['ruangan']] for pasien in data_pasien
            ]
            tampilkan_tabel(pasien_tabel, ["ID Pasien", "Nama", "Jenis Kelamin", "Golongan Darah", "Berat Badan", "Tinggi Badan", "Diagnosa", "Dokter", "Ruangan"])
            id_pasien = valid_input("Masukkan ID Pasien yang ingin dihapus (PSNxxx): ").upper()
            pasien = next((p for p in data_pasien if p['id'] == id_pasien), None)

            if pasien:
                # Pastikan pasien yang akan dihapus ditangani oleh dokter yang sedang login
                if pasien['dokter'] == current_user['nama']:
                    data_pasien = [p for p in data_pasien if p['id'] != id_pasien]
                    simpan_data("data_pasien.json", data_pasien)
                    print("Data pasien berhasil dihapus!")
                else:
                    print("Anda tidak memiliki izin untuk menghapus data pasien ini.")
            else:
                print("Pasien tidak ditemukan!")
            input("Tekan enter untuk kembali...")
        elif pilih == '5':
            # Ganti password
            password_baru = valid_input("Password baru: ")
            while not valid_password(password_baru):
                print("Password harus minimal 8 karakter!")
                password_baru = valid_input("Password baru: ")
            current_user['password'] = password_baru
            simpan_data("data_akun.json", data_akun)
            print("Password berhasil diganti!")
            input("Tekan enter untuk kembali...")
        elif pilih == '6':
            break
        else:
            print("Pilihan tidak tersedia.")

# Fungsi untuk menu guest
def menu_guest(data_pasien, current_user):
    while True:
        clear_screen()
        print("=== Menu Guest ===")
        print("1. Lihat Data Pasien")
        print("2. Ganti Password")
        print("3. Logout")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            # Tampilkan tabel data pasien
            pasien_tabel = [
                [pasien['id'], pasien['nama'], pasien['dokter'], pasien['ruangan']] for pasien in data_pasien
            ]
            tampilkan_tabel(pasien_tabel, ["ID Pasien", "Nama", "Dokter", "Ruangan"])
            input("Tekan enter untuk kembali...")
        elif pilih == '2':
            # Ganti password
            password_baru = valid_input("Password baru: ")
            while not valid_password(password_baru):
                print("Password harus minimal 8 karakter!")
                password_baru = valid_input("Password baru: ")
            current_user['password'] = password_baru
            simpan_data("data_akun.json", data_akun)
            print("Password berhasil diganti!")
            input("Tekan enter untuk kembali...")
        elif pilih == '3':
            break
        else:
            print("Pilihan tidak tersedia.")

# Fungsi login
def login(data_akun):
    kesempatan = 3  # Inisialisasi jumlah percobaan login
    while kesempatan > 0:
        clear_screen()
        print ("== Menu Login ==")
        username = valid_input("Username: ")
        password = valid_input("Password: ")

        user = next((akun for akun in data_akun if akun['username'] == username and akun['password'] == password), None)
        if user:
            return user
        else:
            kesempatan -= 1  # Menambah jumlah percobaan login
            print(f"Username atau password salah. Sisa percobaan : {kesempatan}")
            input("Tekan enter untuk melanjutkan...")
            if kesempatan == 0:
                print("Terlalu banyak percobaan login yang gagal. Program akan berhenti.")
                exit()  # Menghentikan program setelah 3 percobaan gagal

# Fungsi untuk register
def register(data_akun):
    clear_screen()
    print("=== Register ===")
    id_baru = f"GST{len(data_akun) + 1:03d}"
    while True:
        username = valid_input("Username: ")
        # Cek apakah username sudah ada
        if any(akun['username'] == username for akun in data_akun):
            print("Username telah terpakai. Silakan pilih username lain.")
        else:
            break  # Username valid, keluar dari loop

    password = valid_input("Password: ")
    while not valid_password(password):
        print("Password harus minimal 8 karakter!")
        password = valid_input("Password: ")

    guest_baru = {
        "id": id_baru,
        "username": username,
        "password": password,
        "role": "guest",
    }
    data_akun.append(guest_baru)
    simpan_data("data_akun.json", data_akun)
    print("Akun guest berhasil dibuat!")
    input("Tekan enter untuk kembali...")

# Program utama
def main():
    data_akun = muat_data("data_akun.json")
    data_pasien = muat_data("data_pasien.json")

    while True:
        clear_screen()
        print("=== Selamat Datang di Sistem Rumah Sakit ===")
        print("1. Login")
        print("2. Register (guest)")
        print("3. Keluar")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            user = login(data_akun)

            if user['role'] == 'admin':
                menu_admin(data_akun, data_pasien)
            elif user['role'] == 'dokter':
                menu_dokter(data_pasien, data_akun, user)
            elif user['role'] == 'guest':
                menu_guest(data_pasien, user)
        elif pilih == '2':
            register(data_akun)
        elif pilih == '3':
            clear_screen()
            print("Terimakasih telah menggunakan program!")
            break
        else:
            print("Pilihan tidak tersedia.")

main()