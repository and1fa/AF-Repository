# data_mhs ={
#     "nama" : "ucup",
#     "nim" : 1,
#     "matkul" : ["kalkulus", "apd"],
#     "dosen" : {
#         "nama" : "pak awang",
#         "matkul" : "apd"
#     }

# }

# print(data_mhs["dosen"]["nama"])

data_mhs = [
    {
     "nama" : "usup",
     "role" : "admin"
     },

     {
     "nama" : "michael",
     "role" : "user"
     }
]

print(data_mhs[0]['nama'])
print(data_mhs[1]['nama'])


# for value in data_mhs():
#     print(value)

# for value in data_mhs.values():
#     print(value)

# print("Jumlah Data = ", len(data_mhs))

# del data_mhs ["nim"]

# cache = data_mhs.pop("nim")

# print(data_mhs, "Dictionary")
# print(cache, "cache")

# data_mhs["id"]= cache
# print(data_mhs)

# print(data_mhs.clear(), "clear")

# data_mhs['alamat']="Samarinda"
# data_mhs['alamat']="Tenggarong"

# data_mhs.update({"alamat": "Samarinda"})
# data_mhs.update({"alamat": "Tenggarong"})


# data_mhs['nama']="ahmad"





# print(data_mhs['nama'])
# print(data_mhs['nim'])

# print(data_mhs.get("Alamat", "Key tersebut tidak ada"))

# for data in data_mhs:
#     print(data)   

# for key_data, value_data in data_mhs.items():
#     print(f"Key: {key_data}\nvalue: {value_data} \n") 

# key = "apel", "jeruk", "mangga", "semangka", "anggur"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)


Nilai = {
    "Matematika" : 80,
    "B. Indonesia" : 90,
    "B. Inggris" : 81,
    "Kimia" : 20
}
# #sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)


