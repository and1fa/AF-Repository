import os

data_mahasiswa = ["Ifnu", "Adi", "Ucup", "Michael"]

def clear_screen():
    os.system('cls || clear')

clear_screen()

def tampilkan_mahasiswa(data):
    for i in range(len(data)):
        print(f"Data ke {i+1}")
        print(f"Nama : {data[i]}")
        print("="*10)

def tambah_data(data, inputUser):
    print("MENU TAMBAH DATA")
    print("=" * 10)
    data.append(inputUser)
    print(f"{inputUser} telah ditambahkan")
    return data

def ubah_data(data, index, data_baru):
    if 1 <= index <= len(data):
        data[index-1] = data_baru
        print("Data berhasil diubah")
    else:
        print("Index tidak valid")
    return data

def hapus_data(data, index):
    if 1 <= index <= len(data):
        del_user = data.pop(index-1)
        print(f"{del_user} telah dihapus")
    else:
        print("Index tidak valid")
    return data

def menu():
    print("""
    Menu
    1. Lihat Data
    2. Tambah Data
    3. Edit Data
    4. Hapus Data
    5. Keluar
    """)

clear_screen()

while True:
    menu()
    pilih = input("Masukan Pilihan menu >> ")
    clear_screen()
    
    if pilih == "1":
        print("=== Lihat Data ===")
        tampilkan_mahasiswa(data_mahasiswa)
        input("Enter.....")
        clear_screen()
    elif pilih == "2":
        inputUser = input("Data yang mau ditambahkan: ")
        data_mahasiswa = tambah_data(data_mahasiswa, inputUser)
        input("Enter....")
        clear_screen()
    elif pilih == "3":
        print("=== Menu Ubah Data ===")
        tampilkan_mahasiswa(data_mahasiswa)
        index = int(input("Masukkan index yang mau diedit: "))
        data_baru = input("Masukkan nama baru: ")
        data_mahasiswa = ubah_data(data_mahasiswa, index, data_baru)
        input("Enter.....")
        clear_screen()
    elif pilih == "4":
        print("=== Menu Hapus Data ===")
        tampilkan_mahasiswa(data_mahasiswa)
        index_user = int(input("Masukkan index yang ingin dihapus: "))
        data_mahasiswa = hapus_data(data_mahasiswa, index_user)
        input("Enter......")
        clear_screen()
    elif pilih == "5":
        print("Anda memilih untuk keluar. Sampai jumpa!")
        break
    else:
        print(f"Menu {pilih} tidak tersedia")
        input("Enter.....")
        clear_screen()
