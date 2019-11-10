Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = "Dimas Ibnu Rahmadhani"
>>> NIM = "L200190178"
>>> X = "1" + NIM[7:]
>>> a = int (X)
>>> b = len(Nama)
>>> type (a)
<class 'int'>
>>> #Karena data "X" telah berubah menjadi data bertype integer.
>>> type (b)
<class 'int'>
>>> #Karena data "Nama" memiliki intruksi "len"
>>> a / b
56.095238095238095
>>> #Karena hasil bagi dari 1178 dibagi 21 adalah 56.095238095238095
>>> a // b
56
>>> #Karena arti dari "//" adalah hasil pembagian yang dibulatkan.
>>> 10 * (a - 999)
1790
>>> #Karena nilai "a" dikurangi 999 adalah 179, kemudian hasil pengurangan tersebut dikalikan dengan 10 dan hasilnya adalah 1790.
>>> b ** 2
441
>>> #Karena simbol dari "**" adalah perpengkatan.
>>> a % b
2
>>> #Karena simbol dari "%" adalah sisa dari hasil pembagian.
>>> c = 12.5
>>> type (c)
<class 'float'>
>>> #Karena 12.5 adalah bentuk desimal.
>>> a / c
94.24
>>> #Karena hasil bagi dari 1178 dibagi 12.5 adalah 94.24
>>> a // c
94.0
>>> #Karena arti simbol "//" adalah pembagian yang dibulatkan.
>>> a % c
3.0
>>> #Karena arti "%" adalah sisa dari hasil pembagian dan sisa hasil pembagian 1178 dibagi 12.5 adalah 3.0
>>> c > b
False
>>> #Karena nilai "c" lebih besar dari nilai "b" adalah salah.
>>> type(c > b)
<class 'bool'>
>>> #Karena c > b hanya memiliki dua kemungkinan yaitu true jika benar dan false jika salah.
>>> a > b and b > c
True
>>> #Karena logika "DAN" true and true menghasilkan nilai true.
>>> a > 1100 or b < 10
True
>>> #Karena logika "ATAU" true or false menghasilkan nilai true.
