# inisialisi
makanan = ["nasi","ikan","ayam","sayur"]

#read 
#readALl value
print(f"ini data dalam list : {makanan}")
#read spesifik
#index mulai dari 0 
print(f"isi dari index ke 3 : {makanan[3]}")
print(f"isi dari index ke -2: {makanan[-2]}")

#update
makanan[0] = "buah"
print(f"isi data setelah di update pada list : {makanan}")

#add atau append
makanan.append("makanan_darurat")
print(f"isi data setelah di append pada list : {makanan}")

#delete
makanan.remove("makanan_darurat")
print(f"isi data setelah di delete pada list : {makanan}")

makanan_ringan = ["ciki","seblak"]
makanan += makanan_ringan
print(f"isi data setelah di tambahakan jensi baru pada list : {makanan}")