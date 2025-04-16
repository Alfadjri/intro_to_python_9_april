siswas = {
    "kelas" : 12,
    "jurusan" : [["Biologi","Kimia","Fisika"],'IPS'],
    "nama_ketua" : "Udin"
}

# Read all
print(f"Data metah : {siswas}")
# erea spesifik value
print(f"Ambil value dari kelas : {siswas["kelas"]}")
print(f"Ambil value dari jurusan siswa : {siswas["jurusan"][1]}")
print(f"Ambil valeu dari jurusan IPA index ke 2 : {siswas["jurusan"][0][2]}")
#add atau append
siswas["nilai"] = [10,40,30]
print(f"Data metah setelah di add : {siswas}")

#update
siswas["nilai"][1] = 20
print(f"Data metah setelah di update : {siswas}")
#delete
del siswas["nilai"]
print(f"Data metah setelah di delete : {siswas}")

