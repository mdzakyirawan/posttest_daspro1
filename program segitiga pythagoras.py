import math

print('LOGIN')
print('Masukkan NIM, NAMA, KELAS dan ANGKATAN anda')
print ('========================================')
NIM = int(input('NIM       :'))
NAMA = input('NAMA      :')
KELAS = input('KELAS     :')
ANGKATAN = int(input('ANGKATAN  :'))
print ('========================================')

if NIM == 2309116031 and NAMA == 'MUHAMMAD DZAKY IRAWAN' and KELAS == 'A' and ANGKATAN == 23:
    print('Selamat datang Muhammad Dzaky Irawan')
    print ('========================================')

    print('Pilihan operasi pythagoras')
    print('1. Alas')
    print('2. Sisi Tegak')
    print('3. Sisi Miring')
    print('----------------------------------------')
    operasi = int(input('Pilihan anda:'))
    print('----------------------------------------')
    
    if operasi == 1:
        print('untuk menghitung alas, masukkan panjang sisi tegak dan sisi miring\n');
        sisi_tegak = int(input('panjang sisi tegak:'))
        sisi_miring = int(input('panjang sisi miring:'))
        alas = math.sqrt(sisi_miring**2 - sisi_tegak**2)
        print('Jadi, panjang sisi alas adalah', alas)
    elif operasi == 2:
        print('untuk menghitung sisi tegak, masukkan panjang sisi miring dan alas\n')
        sisi_miring = int(input('panjang sisi miring:'))
        alas = int(input('panjang alas:'))
        sisi_tegak = math.sqrt(sisi_miring**2 - alas**2)
        print('Jadi, panjang sisi tegak adalah', sisi_tegak)
    elif operasi == 3:
        print('untuk menghitung sisi miring, masukkan panjang sisi tegak dan alas\n')
        sisi_tegak = int(input('panjang sisi tegak:'))
        alas = int(input('panjang alas:'))
        sisi_miring = math.sqrt(alas**2 + sisi_tegak**2)
        print('Jadi, panjang sisi sisi miring adalah', sisi_miring)
    else:
        print('tidak valid')
else:
    print('Gagal login')
