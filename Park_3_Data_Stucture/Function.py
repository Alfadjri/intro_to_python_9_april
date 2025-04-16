# function void 
# function yang tidak akan pengaruh apapun 
def cetak_nilai(pesan_yang_mau_di_sampaikan = None , value = None):
    print(f"Ambil data dari {pesan_yang_mau_di_sampaikan} : {value}")
    
# fucntion bertipe data
def diskon(harga_asli,persentase_diskon):
    diskon = persentase_diskon / 100
    harga_diskon = harga_asli - (diskon * harga_asli)
    harga_asli -= harga_diskon
    return harga_asli

#contoh data 
siswas = {
    "kelas" : 12,
    "jurusan" : [["Biologi","Kimia","Fisika"],'IPS'],
    "nama_ketua" : "Udin"
}

#pakek function
cetak_nilai("jurusan IPA",siswas["jurusan"][0][2])
cetak_nilai("Kelas",siswas["kelas"])

#contoh data 
harga_barang = 100000
diskon_barang = 20
harga_akhir = diskon(harga_barang,diskon_barang)
print(f"Dari harga barang {harga_barang} setelah di diskon {diskon_barang}% menjadi : {harga_akhir}")