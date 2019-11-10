Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Dimas Ibnu Rahmadhani"
>>> NIM = 178
>>> Tinggi = 1.72
>>> Berat = 49
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type (Aku)
<class 'tuple'>
>>> #Merupakan data bertipe tuple yang berisi sekumpulan data yang memuat TahunLahir, Berat, Tinggi, NIM, dan Nama dan tipe data tuple tidak dapat diubah.
>>> Aku [0]
2000
>>> #Menampilkan elemen tuple indeks ke-0 yaitu "TahunLahir" atau data yang berisi 2000
>>> a = NIM % 4; Aku[a]
1.72
>>> #Hasil sisa bagi dari variabel NIM dibagi 4 adalah 2 dan disimpan dalam variabel a kemudian Aku[a] akan menjadi Aku[2] dimana akan menampilkan elemen tuple Aku indeks ke-2 atau "Tinggi".
>>> type(Aku[a])
<class 'float'>
>>> #Elemen tuple Aku indeks ke 2(2 merupakan data dari variabel a) atau "Tinggi" adalah 1.72 dan merupakan data bertipe float atau bilangan desimal.
>>> Aku[a:4]
(1.72, 178)
>>> #Menampilkan elemen dari tuple Aku mulai dari indeks ke-2 hingga sebelum indeks ke-4 yang berisi Tinggi dan NIM.
>>> type(Aku[4])
<class 'str'>
>>> #Elemen tuple Aku indeks ke-4 merupakan data tipe string karena berisi "Nama".
>>> Aku[0] = "ok"
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = "ok"
TypeError: 'tuple' object does not support item assignment
>>> #Terjadi tipe eror karena data tipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' maka terjadi tipe error.
>>> type(Data)
<class 'list'>
>>> #Variabel Data merupakan data bertipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah.
>>> type(Data[4])
<class 'str'>
>>> #Elemen list indeks ke-4 atau yang berisi "Nama" merupakan data yang bertipe string karena mengandung karakter.
>>> Data[4][5]
' '
>>> #Elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu spasi(" ").
>>> Data[4][a:6]
'mas '
>>> #Elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 2 maka akan menjadi Nama[2:6] yang akan menampilkan elemen list indeks ke-2 hingga sebelum indeks ke-6 yaitu "mas ".
>>> Data[0] = "ok"; Data
['ok', 49, 1.72, 178, 'Dimas Ibnu Rahmadhani']
>>> #Elemen list Data indeks ke-0 diubah dari "TanggalLahir" menjadi 'ok' dan kemudian program menampilkan data dari list Data.
>>> Data[-a]
178
>>> #Variabel a berisi data 2 maka program menjadi Data[-2] yang akan menampilkan elemen list Data indeks ke-3 atau (-2).
>>> range(a)
range(0, 2)
>>> #Varibel a berisi data 2 maka program akan menjadi range(2) dan program akan menampilkan range dari 0 hingga 2 atau jika ditulis dalam program range(0, 2).
