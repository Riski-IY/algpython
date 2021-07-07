"""
Cek nilai Loop 
" Loop Program perhitungan gaji karyawan CV.LOGOS
" loop program (run)
"""
#CEK Program 
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("               //PERHITUNGAN GAJI KARYAWAN CV. LOGOS\\                ")
    print("")
    print("======================================================================")
    print("======================================================================")
    #input nama karyawan,jenis kelamin,dan status  
    Karyawan = input("Masukan Nama Karyawan          : ")
    
    #input gaji pokok
    ringajipokok = ['Golongan 1 = 2.500.000','Golongan 2 = 4.500.000','Golongan 3 = 6.500.000']
    golongan = ['Golongan 1','Golongan 2','Golongan 3']
    gajipokok = [2500000,4500000,6500000]
    
    pilihan = input("Masukkan Golongan              : ")
    #identifikasi pilihan
    if pilihan=="1":
        idx = 0
        tunjanganistri = 2500000*0.01
    elif pilihan=="2":
        idx = 1
        tunjanganistri = 4500000*0.03
    elif pilihan=="3":
        idx = 2
        tunjanganistri = 6500000*0.05
    else:
        idx = 4
        print("Mohon maaf data golongan yang anda inputkan TIDAK TERDAFTAR")
        
    #cetak gaji pokok
    print("Perincian gaji pokok           : " + ringajipokok[idx])
    
    #menghitung tunjangan istri
    jeniskelamin = input("Masukan Jenis Kelamin          : " )
    statuskawin = input("status kawin / belum kawin     : ")
    if jeniskelamin=="laki-laki" and statuskawin=="kawin":
        print("=> Total untuk tunjangan istri = Rp " + str(tunjanganistri))
             
    #menghitung tunjangan anak
    gajipokok = gajipokok[idx]
    tunjangananak = gajipokok*0.02
    #tampilkan
    mempunyaianak = input("punya anak / belum punya anak  :")
    if statuskawin=="kawin" and mempunyaianak=="punya anak":
       print("=> Total untuk tunjangan anak  = Rp " + str(tunjangananak))
    
    #menghitung gaji bruto
    gajibruto = gajipokok+tunjangananak+tunjanganistri
    #tampilkan
    print("=> Gaji bruto                  = Rp " + str(gajibruto))
    
    #menghitung biaya jabatan
    biayajabatan = gajibruto*0.005
    print("=> Biaya jabatan               = Rp " + str(biayajabatan))
    
    #menghitung iuran pensiun
    iuranpensiun = 15500
    print("=> Iuran pensiun karyawan      = Rp 15.500 " )
    
    #menghitung iuran organisasi
    iuranorganisasi = 3500
    print("=> Iuran organisasi            = Rp 3.500 " )
    
    #menghitung gaji netto
    gajinetto = gajibruto-biayajabatan-iuranpensiun-iuranorganisasi
    print("=> Gaji netto                  = Rp " + str(gajinetto))
    print("======================================================================")
    print("======================================================================")
    print("")

    #membuat slip gaji
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("=           ..::SLIP GAJI KARYAWAN::..             =")
    print("=                ..::CV. LOGOS::..                 =")
    import datetime
    x = datetime.datetime.now()
    print(" Tanggal : " + str(x))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   Nama karyawan   :" + Karyawan)  
    print("   Golongan        :" + golongan[idx])
    print("   Jenis kelamin   :" + jeniskelamin)
    print("   Status kawin    :" + statuskawin)
    print("   Gaji Pokok      : Rp " + str(gajipokok))
    if jeniskelamin=="laki-laki" and statuskawin=="kawin":
        print("   Tunjangan Istri : Rp " + str(tunjanganistri))
    if statuskawin=="kawin" and mempunyaianak=="punya anak":    
        print("   Tunjangan Anak  : Rp " + str(tunjangananak))
    print("=> Gaji Bruto = Rp " + str(gajibruto))
    print("____________________________________________________")
    print(" Biaya jabatan    : Rp " + str(biayajabatan))
    print(" Iuran pensiun    : Rp 15.500 " )
    print(" Iuran organisasi : Rp 3.500 " )
    print("=> Gaji Netto = Rp " + str(gajinetto))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")

    #ulangi program y/t
    ulangprog = input(">> INPUT gaji lagi ? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break
    print("") 