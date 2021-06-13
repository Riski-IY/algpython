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

    #Pembelian diatas 1,5 juta diskon 15%
    if total>1500000:
        totalsesudahdiskon=total-15/100*total
        print("=>Mendapatkan diskon 15% = Rp " + str(totalsesudahdiskon))
    
    ulangprog = input("Apakah anda ingin menginputkan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break     