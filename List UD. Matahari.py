"""
Cek nilai Menggunakan Loop 
" Loop CEK Program Bengkel Motor UD.Matahari
" loop run program (ok)
"""
#CEK Program Bengkel Motor UD.Matahari
ulang = "y"
while ulang=="y" or ulang=="Y":
    
    print ("    ..::BENGKEL MOTOR UD. MATAHARI::.. ")
    print ("")
    print ("            Daftar Merk Oli")
    print ("#######################################")
    print (" A. Duration SW20 1L")
    print (" B. Castrol Magnatec 1L")
    print (" C. Federal Supreme XX 1L")
    print (" D. Yamalube 1L")
    print (" E. Shell 1L")
    print ("#######################################")
    print("")
    merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L','-']
    harga = [53000,50000,54000,45000,46000,0]
    
    pilihan = input(" Masukkan Kode Merk Oli = ")
    print ("-------------------------------------------")
    
#pilihan kode
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 5
        pesan = "Mohon maaf harap masukan KODE A/B/C/D"
        print (pesan)
        print("")
    jumlah = int(input(" Jumlah     = "))
        
#tampilan layar
    print(" Merk Oli   = " + merk[idx])
    print(" Harga      = Rp." + str(harga[idx]))
    
#hitung transksi
    fixharga = harga[idx]
    subtotawal = fixharga * jumlah
    if subtotawal > 200000:
        diskon = subtotawal * 0.05
    else:
        diskon = 0
    subtotakhir = subtotawal - diskon
    ppn = subtotakhir * 0.01
    total = subtotakhir - ppn
    print(" diskon     = Rp." + str(diskon))   
    
#total ongkir
    print("-------------------------------------------")
    print(" Subtotal   = Rp." + str(subtotakhir))
    print('-------------------------------------------')
    print("")
    print(" PPN        = Rp." + str(ppn))
    print("")
    print("-------------------------------------------")
    print(" TOTAL      = Rp." + str(total))
    print("")
    print("===========================================")
    print("      TERIMA KASIH ATAS PEMBELIAN ANDA     ")
    print("===========================================")
    print("barang yang sudah dibeli tidak dapat ditukar")
    jawab = input (" ULANGI PROGRAM ? Y/T = ")
    print("")
    print("")
    print("")
    if jawab == "t" or jawab =="T":
        break