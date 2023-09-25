print('===========================')
print('SELAMAT DATANG DI UBSI MART')
print('===========================')


def hitung_nasi():
    print('hitung harga nasi: ')
    jumlah_nasi = int(input('masukan jumlah: '))
    harga_nasi = 5000
    total_nasi = jumlah_nasi*harga_nasi
    print('harga total makanan mu: rp.', total_nasi,'\n')

def hitung_babi():
    print('hitung harga babi: ')
    jumlah_babi = int(input('masukan jumlah: '))
    harga_babi = 15000
    total = jumlah_babi*harga_babi
    print('harga total makanan mu : rp.', total,'\n')

def hitung_ayam():
    print('hitung harga ayam: ')
    jumlah_ayam = int(input('masukan jumlah: '))
    harga_ayam = 10000
    total = jumlah_ayam*harga_ayam
    print('harga total makanan mu : rp', total,'\n')

def hitung_ikan():
    print('hitung harga nasi: ')
    jumlah_ikan = int(input('masukan jumlah: '))
    harga_ikan = 12000
    total = jumlah_ikan*harga_ikan
    print('harga total makanan mu : rp.', total,'\n')

def bayar():
    print('masukan pembayaran')
    bayar = int(input('bayar tunai :'))
    bayar = bayar - hitung_nasi()
    
    if bayar < hitung_nasi():
        print('maaf saldo anda tidak mencukupi')
    else:
        print('terimakasih atas pesanannya')
        


while True:
    userinput = int(input('\npilih makanan yang akan dimakan: \n\n1.nasi\n2.babi\n3.ayam\n4.ikan\n\n0.keluar program\n\npilih nomor berapa: '))
        #nasi
    if(userinput == 1):
        hitung_nasi()
        #harga babi
    if(userinput == 2):
        hitung_babi()
        #harga ayam
    if(userinput == 3):
        hitung_ayam()
        #harga ikan
    if(userinput == 4):
        hitung_ikan()
        #pembayaran
    if(userinput == 1):
        bayar()

    else:
        break


