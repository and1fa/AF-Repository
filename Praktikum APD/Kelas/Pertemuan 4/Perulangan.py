# batas = 20
# for i in range(1, batas, 2):
#     print (f"Perulangan ke-{i}")


# buah_banyak = ["apel", "mangga", "anggur"]
# for buah in buah_banyak:
#     print (buah)

# for baris in range (1,4):
#     print("baris ke", baris)
#     for kolom in range (1,4):
#         print(kolom, "kolom", end=" ")
#     print()
#     print()

# while True:
#     print ("Hello") 
# # infinit while

# lagi = "yes"
# ulang = 0
# while lagi == "yes":
#     ulang += 1
#     print ("Mabar") 
#     lagi = input ("mabar lagi gak")
# print("Selesai")
# print(f"perulangan terjadi sebanyak {ulang} kali")

# for i in range(1,10):
#     if i ==4:
#         break
#     else:
#         print(f"Perulangan ke-{i}")

# while True:
#     ulang = input("mabar lagi: ")
#     if ulang == "gk":
#         break
#     print ("mabar lagi")

# for i in range (1,10):
#     if i == 4:
#         continue
#     print(f"perulangan ke- {i}")

# total = 0
# while True:
#     angka = int(input("Masukkan angka : "))
#     if angka < 0:
#         break
#     total += angka

# print(f"Jumlah total angka positif adalah: {total}")



# for i in range(1,6):
#     print("*" *i)


kesempatan = 3

while kesempatan > 0:
    username = input("masukkan username: ")
    password = input("masukkan password: ")

    if username == "admin" and password=="admin":
        print ("berhasil login")
        break
    else:
        print("username atau password salah")
        kesempatan -=1
        print(f"kesempatan login sisa {kesempatan} kali")

print("Program Utama")


