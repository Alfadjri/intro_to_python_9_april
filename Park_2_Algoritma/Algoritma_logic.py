nilai_raport = 100
# teknik ini di gunakan kalau kamu ragu dengan nilai kondisi yang akan terjadi
print("============if============")
#if 
#format dasar
#if(kondisi):
#   apa yang kamu mau lakukan jika nilainya terpenuhi


if (nilai_raport >= 100):
    print("Selamat kamu lulus dengan nilai sempurna")
    
print("============if-else============")
nilai_raport = 65
#if else
# format dasar
#if (kondisi terpenuhi):
# apa yang kamu mau lakukan jika nilainya terpenuhi
#else:
# kondisi di mana jika tidak terpenuhi melakukan apa dan ini secara paksa
if (nilai_raport <= 100):
    print("Selamat kamu lulus dengan nilai sempurna")
else : 
    print("Mohon Maaf anda mengulang lagi di kelas ini !")

# if bersarang
# teknik ini tidak di sarankan  karna memikirkan yang benar
if (nilai_raport <= 100):
    if (nilai_raport >= 60):
        if (nilai_raport >= 65):
            print("Kamu lulus pernaiki nilai mu karna dikit lagi kamu gagal ")
        else :
            print("Hampir saya kamu tidak lulus!")
    else :
        print("Selamat kamu lulus dengan nilai sempurna")
else : 
    print("Mohon Maaf anda mengulang lagi di kelas ini !")
# teknik black list 

#teknik singkat
#teknik yang kamu gunakan kalau nilainya sederhana  atau singkat
print("============if-else (tenery)============")
nilai_raport = 100
pesan = "A" if nilai_raport >= 100 else "C"
print(f'NIlai Kamu : {pesan}')


# switch case
# di pakai di menu makusdnya kondisi di mana user hanya memilih 1 tombol atau 1 nilai
print("============switch case============")
print("=====Menu Selection =======")
print("1.Start")
print("2.exit")
selection = input("Select => ")
match(selection):
    case "1":
        print("Start Game")
    case "2":
        print("Exit")
    case _:
        print("Input tidak tersedia")