import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50009))
s.listen(5)
print "Server sudah siap"
perintah = ''
a=0
while perintah != 'keluar':
    komm, addr = s.accept()
    while perintah != 'keluar':
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == 'keluar':
            komm.send('done')
            s.close()
            break
        print "pesan: ", perintah
        if len(item)==2:
            if perintah == 'sisi':
                a=int(item[1])
                komm.send('sisi disimpan')
            else:
                komm.send('Pesan tidak diketahui')
        elif perintah == 'hitung':
            L=float(2*a)
            response = 'Luas persegi dengan sisi {} adalah{}' .format(a,L)
            komm.send(response)
        else:
            komm.send('Pesan tidak diketahui')
