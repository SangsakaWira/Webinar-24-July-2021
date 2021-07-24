#  Program mencari luas persegi panjang
# int * int, float * float, int * float dll
panjang = input("Masukkan nilai panjang: ")
lebar = input("Masukkan nilai lebar: ")
luas = float(panjang) * float(lebar)
print(round(luas, 2))
print(float("{:.2f}".format(luas)))
print("%0.2f" % luas)