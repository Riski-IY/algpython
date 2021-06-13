"""
Program cek kelulusan dengan Loop 
" loop run program (ok)
"""
#Mengecek kelulusan: jika nilai di atas 60 maka LULUS, selain itu TIDAK LULUS
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("       ..::PERIKSA KELULUSAN::..        ")
    #setiap dari value yang diinput, akan bertipe data STRING
    n = input ("Masukan Nilai = ")
    u = int(n)
    #cek nilai
    if int(u)>60:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"
          
    print (status)   

    ulangprog = input(">> Apakah anda ingin menginputkan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break