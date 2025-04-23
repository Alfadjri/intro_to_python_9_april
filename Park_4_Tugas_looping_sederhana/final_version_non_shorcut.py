# Fungsi bantu untuk cetak karakter per baris
def cetak_line(char, jumlah):
    for _ in range(jumlah):
        print(char, end='')  # Tidak menggunakan 'end', tapi kita tetap cetak baris baru setiap kali
    print()  # Pindah ke baris baru setelah selesai

# ====================
# SEGITIGA GENERIK
# ====================
def segitiga_kiri_bawah(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end='')
        print()  # Pindah ke baris baru setelah setiap baris

def segitiga_kanan_bawah(n):
    for i in range(1, n + 1):
        for s in range(n - i):
            print(' ', end='')  # Spasi di depan
        for j in range(i):
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

def segitiga_kiri_atas(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

def segitiga_kanan_atas(n):
    for i in range(n, 0, -1):
        for s in range(n - i):
            print(' ', end='')  # Spasi di depan setiap baris
        for j in range(i):
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

# ====================
# DIAMOND BINTANG
# ====================
def diamond_bintang(n):
    # Bagian atas
    for i in range(1, n + 1):
        for s in range(n - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()  # Pindah ke baris baru setelah setiap baris

    # Bagian bawah
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print('*', end='')
        print()  # Pindah ke baris baru setelah setiap baris

# ====================
# DIAMOND PINGGIR KOSONG
# ====================
def diamond_pinggir(n):
    # Bagian atas
    for i in range(1, n + 1):
        for s in range(n - i):
            print(' ', end='')
        print('*', end='')
        if i > 1:
            for kosong in range(2 * i - 3):
                print(' ', end='')
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

    # Bagian bawah
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(' ', end='')
        print('*', end='')
        if i > 1:
            for kosong in range(2 * i - 3):
                print(' ', end='')
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

# ====================
# DIAMOND PINGGIR DARI KIRI-KANAN (mirror)
# ====================
def diamond_kiri_kanan(n):
    for i in range(1, n + 1):
        for s in range(n - i + 1):
            print('*', end='')
        for t in range(2 * i - 2):
            print(' ', end='')
        for s in range(n - i + 1):
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

    for i in range(n - 1, 0, -1):
        for s in range(n - i + 1):
            print('*', end='')
        for t in range(2 * i - 2):
            print(' ', end='')
        for s in range(n - i + 1):
            print('*', end='')
        print()  # Pindah ke baris baru setelah selesai

# ====================
# POHON CEMARA
# ====================
def pohon_cemara(n):
    tinggi = max(2, n // 4)  # Menentukan tinggi level pohon
    for level in range(1, 4):
        for i in range(1, tinggi + level):
            for _ in range(n - i):  # Spasi kiri
                print(' ', end='')
            for _ in range(2 * i - 1):  # Bintang tengah
                print('*', end='')
            print()  # Pindah ke baris baru setelah selesai

    # Bagian batang pohon
    for i in range(n // 5):
        for _ in range(n - 1):  # Spasi kiri batang
            print(' ', end='')
        print('||')  # Batang pohon

# ====================
# CONTOH PEMANGGILAN
# ====================
n = 5
print("Segitiga Kiri Bawah:")
segitiga_kiri_bawah(n)

print("\nSegitiga Kanan Bawah:")
segitiga_kanan_bawah(n)

print("\nSegitiga Kiri Atas:")
segitiga_kiri_atas(n)

print("\nSegitiga Kanan Atas:")
segitiga_kanan_atas(n)

print("\nDiamond Bintang:")
diamond_bintang(n)

print("\nDiamond Pinggir Kosong:")
diamond_pinggir(n)

print("\nDiamond Mirror Kiri-Kanan:")
diamond_kiri_kanan(n)

print("\nPohon Cemara:")
pohon_cemara(20)
