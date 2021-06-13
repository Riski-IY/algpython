"""
Mengecek Nilai Dengan Loop 
" Loop cek inputan range bilangan bulat harus >0-100
" loop run program (ok)
"""
#Mengecek nilai
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("     ..::MENAMPILKAN KETERANGAN NILAI::..        ")
    u=1
    while int(u)>0 and int(u)<=100:
        u = input("Masukan Nilai = ")
        #Mengecek bilangan dari 0-100
        if int(u)>0 and int(u)<=100:
            if int(u)>80:
                status="=>BAIK SEKALI"
            elif int(u)>=65:
                 status="=>BAIK" 
            elif int(u)>=55:
                 status="=>CUKUP"   
            elif int(u)>=40:
                 status="=>KURANG"   
            else:
                status="=>KURANG SEKALI"
            print  (status)  

            ulangprog = input("Apakah anda ingin menginputkan lagi? y/t = ")  
            if ulangprog=="t" or ulangprog=="T":
                break 
        #Tampilakan pesan jika angka yang diinputkan tidak sesuai    
        else:
            pesan="Mohon maaf harap memasukan bilangan bulat antara 0-100 :)" 
            print(pesan)
            break        