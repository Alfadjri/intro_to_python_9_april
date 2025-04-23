import os # ini di sebut liblary , header , pakage
import platform

def clear_terminal():
    os_name = platform.system()
    if (os_name == "Windows"):
        os.system('cls')
    else:
        os.system("clear")
def error_input(pesan = "Inputan yang anda lakukan tidak sesuai"):
    input(pesan)

# membuat segitiga siku" baiki poisinya dari kanan bawah , kiri bawah , atas kanan , bawah kanan
def segitiga_siku_siku_kiri_bawah(baris):
    for i in range(1, baris + 1):
        for j in range(i):
            print("*",end=" ")
        print()

def segitiga_siku_siku_kanan_bawah(baris):
    for i in range(1,baris+1):
        for j in range(baris - i):
            print(' ',end=' ')
        for k in range(i):
            print("*",end=" ")
        print()
        

def segitiga_siku_siku_kiri_atas(baris):
    for i in range(baris,0,-1): #kunci untuk posisi kanan atau kiri
        for j in range(i):
            print('*',end=" ")
        print()

def segitiga_siku_siku_kanan_atas(baris):
    for i in range(baris,0,-1): #kunci
        for j in range(baris - i):
            print(' ',end=' ')
        for k in range(i):
            print("*",end=" ")
        print()

def menu_segitiga():
    clear_terminal()
    banyak_baris = 5
    print("=======Segitiga Siku-Siku========")
    print("1.kiri bawah")
    print("2.kanan bawah")
    print("3.kiri atas")
    print("4.kanan atas")
    print("5.Back")
    selection = input("Posisi Print (1,2,3,4) => ")
    match(selection):
        case "1":
            segitiga_siku_siku_kiri_bawah(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "2":
            segitiga_siku_siku_kanan_bawah(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "3":
            segitiga_siku_siku_kiri_atas(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "4":
            segitiga_siku_siku_kanan_atas(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "5":
            return
        case _:
            error_input()
        
    posisi_segitiga() 

def diamon_light(baris):
    for i in range(1, baris + 1):
        for s in range(baris - i):
            print(" ",end=" ")
        for j in range(2 * i - 1):
            print("*",end=" ")
        print()
    
    for i in range(baris - 1, 0 , -1):
        for s in range(baris - i):
            print(" ",end=" ")
        for j in range(2 * i - 1):
            print("*",end=" ")
        print()
        
def diamon_dark(baris):
    for i in range(1,baris + 1):
        for s in range(baris - i + 1):
            print("*",end=" ")
        for j in range(2 * i - 2):
            print(" ",end=" ")
        for s in range(baris - i + 1):
            print("*",end=" ")
        print()
        
    for i in range(baris - 1, 0 , -1):
        for s in range(baris - i + 1):
            print("*",end=" ")
        for j in range(2 * i - 2):
            print(" ",end=" ")
        for s in range(baris - i + 1):
            print("*",end=" ")
        print()

        
        

def menu_diamon():
    banyak_baris = 5
    print("=======Diamon========")
    print("1.light")
    print("2.dark")
    print("3.Back")
    selection = input("Posisi Print (1,2,3) => ")
    match(selection):
        case "1":
            diamon_light(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "2":
            diamon_dark(banyak_baris)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "3":
            return
        case _:
            error_input()
    
    menu_diamon()

def pohon_cemara(baris):
    tinggi = max(2,baris // 4)
    for level in range(1,4):
        for i in range(1 , tinggi + level):
            for j in range(baris - i):
                print(" ", end=" ")
            for j in range(2 * i - 1):
                print("*",end=" ")
            print()
    for i in range(baris // 5):
        for j in range(baris - 1):
            print(" ",end=" ")
        print("|")
    
def menu_pohon_cemara():
    clear_terminal() 
    banyak_baris = 11
    print("=======Pohon Cemara========")
    pohon_cemara(banyak_baris)
    print("3.Back")
    selection = input("Posisi Print (1,2,3) => ")
    match(selection):
        case "3":
            return
    menu_pohon_cemara()

def fibonaci(data, status = False):
    clear_terminal()
    awal_fobonaci = [0,1]
    for i in range(2,data):
        next_fibonaci = awal_fobonaci[-1] + awal_fobonaci[-2]
        awal_fobonaci.append(next_fibonaci)
    if status != False : 
        print(f"Deret fibonaci value : {awal_fobonaci[:data]}")
    
    return awal_fobonaci

def fibonaci_segitiga_siku(data):
    bilangan_fobonaci = fibonaci(data)
    index = 0 
    row = 1
    
    while index < len(bilangan_fobonaci):
        for _ in range(row):
            if index < len(bilangan_fobonaci):
                print(bilangan_fobonaci[index], end=" ")
                index+=1
        print()
        row +=1

def menu_fibonaci():
    clear_terminal()
    jumlah_data = int(input("Masukan jumlah fibonaci yang akan di print : "))
    if jumlah_data <= 0 :
        error_input("Masukan angak lebih dari 0")
        menu_fibonaci()
    jumlah_data += 1
    clear_terminal()
    print("=======Fibonaci========")
    print("1.code")
    print("2.segitiga siku-siku")
    print("3.Back")
    selection = input("Posisi Print (1,2,3) => ")
    match(selection):
        case "1":
            fibonaci(jumlah_data)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "2":
            fibonaci_segitiga_siku(jumlah_data)
            error_input("Tekan Enter untuk balik ke menu sebelumnya")
        case "3":
            return
        case _:
            error_input()
    
    menu_fibonaci()

def main():
    # Panel menu
    while(True):
        clear_terminal()
        print("=======Menu Aplikasi========")
        print("1.Segitiga siku-siku")
        print("2.Diamon")
        print("3.Pohon Cemara")
        print("4.Fibonaci")
        print("5.Exit")
        selection = input("Selection => ")
        match(selection):
            case "1" :
                menu_segitiga()
            case "2":
                menu_diamon()
            case "3":
                menu_pohon_cemara()
            case "4":
                menu_fibonaci()
            case "5":
                input("Selamat Tinggal")
                break
            case _:
                error_input()
            
    

if __name__ == "__main__":
    main()