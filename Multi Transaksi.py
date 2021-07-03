ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("    FAKULTAS TEKNOLOGI INFORMASI    ")
    print("           ..::KANTIN::..          ")
    print("")
    print("             MENU MAKANAN dan MINUMAN           ")
    print("================================================")  
    print(" 1. Nasi Goreng ")
    print(" 2. Lontong Goreng ")
    print(" 3. Bakso Goreng ")
    print(" 4. Rujak Goreng ")
    print(" 5. Rujak Bakso ")
    print(" 6. Rujak Bakso Pecel")
    print(" 7. Teh dingin/hangat/panas")
    print(" 8. Kopi Dingin")
    print(" 9. Kopi Teh Panas")
    print(" 10. Coca Cola Dingin")
    print(" 11. Coca cola Panas")
    print("")
    
    #mencatat nama pembeli    
    pembeli = input("Masukkan nama Pembeli: ")
    print ("Nama Pembeli :", pembeli) 
    
    #input menu makanan
    menumakanan = ['Nasi goreng','Lontong goreng','Bakso goreng','rujak goreng','rujak bakso','rujak bakso pecel']
    Hargamakanan = [15000,14900,12900,13000,15000,17000]
    
    pilihan = input("Masukkan nomer untuk melihat menu makanan = ")
    #identifikasi pilihan
    if pilihan=="1":
        idx = 0
    elif pilihan=="2":
        idx = 1
    elif pilihan=="3":
        idx = 2
    elif pilihan=="4":
        idx = 3
    elif pilihan=="5":
        idx = 4        
    elif pilihan=="6":
        idx = 5 
    else:
        idx = 7
        print("Pesanan yang ANDA masukan tidak TERSEDIA") 
        
    print("Menu Makanan = " + menumakanan[idx])
    print("Harga Menu Makanan = Rp " + str(Hargamakanan[idx])) 
    makananygdibeli = menumakanan[idx]

    jumlahporsi=int(input("jumlah porsi yang dibeli = " ))  
    
    #hitung dan tampilakan
    Hargamakanan = Hargamakanan[idx]
    total1 = Hargamakanan * jumlahporsi
    print("Total Harga     = Rp " + str(total1))  
          
    #input minuman
    menuminuman =['teh dingin','kopi dingin','kopi teh panas','Coca cola dingin','Coca cola panas'] 
    hargaminuman =[2500,5000,6500,3500,5000]
    
    pilihan = input(">> Masukkan nomer untuk melihat menu minuman = ")
    #identifikasi pilihan
    if pilihan=="7":
        idx = 0
    elif pilihan=="8":
        idx = 1
    elif pilihan=="9":
        idx = 2
    elif pilihan=="10":
        idx = 3
    elif pilihan=="11":
        idx = 4        
    else:
        idx = 6
        print("Pesanan yang ANDA masukan tidak TERSEDIA")
        
     #cetak tampilan layar
    print(">>> Menu Minuman = " + menuminuman[idx])
    print(">>> Harga Minuman = Rp " + str(hargaminuman[idx])) 
    
    #input jumlah gelas
    jumlahgelas=int(input("masukan jumlah gelas yang dibeli = " ))  
    #hitung transksi
    hargaminuman = hargaminuman[idx]
    total2 = hargaminuman * jumlahgelas
    print("Total Harga     = Rp " + str(total2)) 
    totalsemua= total1 + total2
    print("Total yang harus Dibayar: Rp" + str(totalsemua))

    #pembayaran dan kembalian
    uangpembeli=int(input("Uang Tunai Pembeli: Rp "))
    kembalian= uangpembeli - totalsemua
    print("Kembalian :" + str(kembalian))
    
    #cetak struk
    print("============================================")
    print("=========  K A N T I N   F T I   ===========")
    print("============================================")
    print (" Nama                       :" + pembeli)
    print (" Makanan                    :" + makananygdibeli)
    print (" Harga                      :" + str(Hargamakanan))
    print (" jumlah dibeli              :" + str(jumlahporsi))
    print (" Total Harga Makanan        :" + str(total1))
    print("")
    print (" Minuman                    :" + menuminuman[idx])
    print (" Harga                      :" + str(hargaminuman))
    print (" jumlah dibeli              :" + str(jumlahgelas))
    print ("  Total Harga Minuman       :" + str(total2))
    print ("")
    print (" Tagihan                    : Rp." + str(totalsemua))
    print (" Uang                       : Rp." + str(uangpembeli))
    print (" Kembalian                  : Rp." + str(kembalian))
    print("=====================================================")
    print("=============   SELAMAT MENIKMATI  ==================")
    
    #inputkan lagi atau tidak
    ulangprog = input("Masukan pesanan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break 