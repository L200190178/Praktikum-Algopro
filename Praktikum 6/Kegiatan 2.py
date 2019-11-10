## Program Akun
## Dibuat oleh Dimas Ibnu Rahmadhani L200190178
import random
angka = random.randint(0,1000)

Nama = "Dimas Ibnu Rahmadhani"
TanggalLahir = "14 Desember 2000"
NamaSingkat = Nama[0]+"."+Nama[6]+"."+Nama[11:21]
Username = Nama[0]+TanggalLahir[:2]+TanggalLahir[12:16]
Password = Nama[0:3]+str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
