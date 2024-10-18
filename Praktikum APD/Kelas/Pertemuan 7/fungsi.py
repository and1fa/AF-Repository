# def hasil(nama):
#     print ("hello world " + nama)

# hasil("adi")
# hasil("adri")
# hasil("dimas")


# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     # print(f"luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas}")
#     return luas

# luas_persegi = luas_persegi_panjang(10,5)

# print(luas_persegi)


# nama = "dimas" #variabel global dapat diakses oleh lokal

# def say_hello():
#     # variabel lokal tdk dpt diakses ole global
#     nama = "dafa"
#     print(nama, "dalam fungsi")

# print(nama, "luar fungsi")

# say_hello()

def faktorial (n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
    
print (faktorial(5))
