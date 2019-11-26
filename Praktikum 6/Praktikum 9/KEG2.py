berkas = open("coba1.txt", "w")
berkas.write("L200190178\n")
berkas.write("12/14/2000\n")
berkas.write("Dimas Ibnu Rahmadhani\n")
berkas.write("Karanganyar")
berkas.close()



berkas = open("coba1.txt", "r")
NIM = berkas.readline()
TTL = berkas.readline()
Nama = berkas.readline()
Kota = berkas.readline()


print(Nama)
print(Kota,",", TTL)
print(NIM)
berkas.close()
