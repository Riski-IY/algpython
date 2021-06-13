"""
Mengecek nilai dengan Loop 
" Loop penilaian mahasiswa
" loop run program (ok)
"""
#Penilaian untuk mahasiswa
ulangprog = "y"
while ulangprog=="y" or ulangprog=="Y":
    print("     ..::PENILAIAN MAHASISWA::..       ")
    n = input("Masukan Nilai = ")
    u = int(n)
    if u>=91:
        nilai = "A"
    elif u>=81:
        nilai = "B"
    elif u>=71:
        nilai = "C"
    else:
        nilai= "D"
    
    
    print (nilai)    

    ulangprog = input("Apakah anda ingin menginputkan lagi? y/t = ")  
    if ulangprog=="t" or ulangprog=="T":
        break