#Mengecek transaksi
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":

    print(" TRANSAKSI PEMBELIAN PRINTER ")
    print("      ..::Epson T20::..      ")
    #Masukan jumlah printer
    hargaprinter=660000
    jumlahbeli=input("Jumlah printer yang dibeli = ")

    #Hitung nilai total
    total = int(hargaprinter)*int(jumlahbeli)
    
    print("=>Total Pembelian yang harus dibayar = Rp " + str(total))
    
    ulangprog = input("Apakah anda ingin menginputkan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break     