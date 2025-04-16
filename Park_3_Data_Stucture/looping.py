# tugas nya bisa bikin segitiga siku" di kiri , kanan, atas , bawah
# tugas paling tinggi bikinkan saya pohon cemara
# dengan syarat besar nya itu dinamis misalnya: 10 baris 20 bari , 40 baris dll

# while
# dipakai saat kamu tahu kapan harus berhenti tapi gak tau caranya !
# di check dulu baru di kerjakan 
count = 0
while(count <= 10):
    print(f"{count}.I Love you")
    count += 1
# do while
# ini kondisinya kerjain dulu baru di check

# for
# di pakai kalau tau kapan harus berhenti dan kapan harus mulai
for index in range(1,11):
    print(f"{index}.I Love you")
    

#break : teknik untuk memaksa berhenti putaran loop
#countinue : teknik untuk skip 1 putaran loop
#contoh
#cetak nilai ganjil sampai nilai 40  
bilangan = 1
while(bilangan <= 100):
    if bilangan % 2 == 0:
        bilangan += 1
        continue
    
    print(bilangan)
    bilangan += 1
    
    if bilangan > 40 :
        break