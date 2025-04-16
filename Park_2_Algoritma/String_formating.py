import datetime 
tanggal = datetime.datetime.now()
nama_guru = "Ucok"
nama_universitas = "Jaya Abadi"

nama_pasien = "Alfadjri"
nip_pasien = "2412003"
jurusan_pasien = "Teknik Informatika"

print("==== Contoh menggunakan format lama ====")
print(f"{tanggal}\n\nKepada Yth.\nBapak\\Ibu {nama_guru}\nDi {nama_universitas}\nDEngan hormat,\nYang bertanda tangan di bawah ini :\nNama : {nama_pasien}\nNIP: {nip_pasien}\nJurusan : {jurusan_pasien}")
print()
print("==== Contoh menggunakan format lama ====")
print()
print("{tanggal}\n\nKepada Yth.\nBapak\\Ibu {nama_guru}\nDi {nama_universitas}\nDEngan hormat,\nYang bertanda tangan di bawah ini :\nNama : {nama_pasien}\nNIP: {nip_pasien}\nJurusan : {jurusan_pasien}".format(tanggal = tanggal , nama_guru = nama_guru, nama_universitas = nama_universitas,nama_pasien = nama_pasien, nip_pasien = nip_pasien, jurusan_pasien = jurusan_pasien))