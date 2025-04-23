# Fungsi bantu untuk cetak karakter per baris
def cetak_line(char, jumlah):
    for _ in range(jumlah):
        print(char, end='')  # Tidak menggunakan 'end', tapi kita tetap cetak baris baru setiap kali

# SEGITIGA GENERIK
def segitiga(n, arah='kiri', posisi='bawah'):
    if posisi == 'bawah':
        baris = range(1, n + 1)
    else:
        baris = range(n, 0, -1)

    for i in baris:
        if arah == 'kanan':
            cetak_line(' ', n - i)
        cetak_line('*', i)
        print()

# DIAMOND BINTANG
def diamond_bintang(n):
    for i in range(1, n + 1):
        cetak_line(' ', n - i)
        cetak_line('*', 2 * i - 1)
        print()
    for i in range(n - 1, 0, -1):
        cetak_line(' ', n - i)
        cetak_line('*', 2 * i - 1)
        print()

# DIAMOND PINGGIR KOSONG
def diamond_pinggir(n):
    for i in range(1, n + 1):
        cetak_line(' ', n - i)
        print('*', end='')
        if i > 1:
            cetak_line(' ', 2 * i - 3)
            print('*', end='')
        print()
    for i in range(n - 1, 0, -1):
        cetak_line(' ', n - i)
        print('*', end='')
        if i > 1:
            cetak_line(' ', 2 * i - 3)
            print('*', end='')
        print()

# DIAMOND PINGGIR DARI KIRI-KANAN (mirror)
def diamond_kiri_kanan(n):
    for i in range(1, n + 1):
        cetak_line('*', n - i + 1)
        cetak_line(' ', 2 * i - 2)
        cetak_line('*', n - i + 1)
        print()
    for i in range(n - 1, 0, -1):
        cetak_line('*', n - i + 1)
        cetak_line(' ', 2 * i - 2)
        cetak_line('*', n - i + 1)
        print()

# POHON CEMARA
def pohon_cemara(n):
    tinggi = max(2, n // 4)
    for level in range(1, 4):
        for i in range(1, tinggi + level):
            cetak_line(' ', n - i)
            cetak_line('*', 2 * i - 1)
            print()
    for i in range(n // 5):
        cetak_line(' ', n - 1)
        print('||')

# ===================
# CONTOH PEMANGGILAN
# ===================
n = 5
print("Segitiga Kiri Bawah:")
segitiga(n, 'kiri', 'bawah')

print("\nSegitiga Kanan Bawah:")
segitiga(n, 'kanan', 'bawah')

print("\nSegitiga Kiri Atas:")
segitiga(n, 'kiri', 'atas')

print("\nSegitiga Kanan Atas:")
segitiga(n, 'kanan', 'atas')

print("\nDiamond Bintang:")
diamond_bintang(n)

print("\nDiamond Pinggir Kosong:")
diamond_pinggir(n)

print("\nDiamond Mirror Kiri-Kanan:")
diamond_kiri_kanan(n)

print("\nPohon Cemara:")
pohon_cemara(20)
