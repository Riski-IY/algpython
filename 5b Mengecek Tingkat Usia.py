"""
Cek golongan Usia Menggunakan Loop 
" Loop cek tingkatan usia
" loop run program (ok)
"""
#Mengecek tingkatan usia
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("..::PERIKSA TINGKATAN USIA::..")
    #Memasukan angka untuk usia
    n = input ("Masukan Usia = ")
    u = int(n)
    #Memasukan rumus
    if int(u)>60:
        status = "Lansia"
    elif int(u)>=35:
        status = "Dewasa"
    elif int(u)>=18:
        status = "Pemuda"
    elif int(u)>=15:
        status = "Remaja" 
    else:
        status = "Anak-anak"
        
    print (status)  

    ulangprog = input(">> Apakah anda ingin menginputkan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break