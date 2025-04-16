# tipe data primitif 
# number
# int (integer)
x = 32767
print("ini contoh bilangan integer : {0}".format(x))
# bilangan desimal
# float dan bouble
# float 
f = 10.50234233213123123123123
print("ini contoh bilangan desimal : {0}".format(f))
# compleks
z = 2 + 3j
print("ini contoh bilangan complex : {0}".format(z))


#sqyence type
a = [1,2,3,4]
print (a)
b = (4,5,6,7)
print(b)
c = range(0,5)
print(c)

#type Text
# Karakter 
karakter_A = 'A'
print("Contoh Karkater : {0}".format(karakter_A))
#String
nama_lengkap = "Alfadjri Dwi Fadhilah"
print("Contoh dari tipe data string : {0}".format(nama_lengkap))

# Maping
profile = {
    "name" : "Alfadjri Dwi Fadhilah",
    "age" : 24,
    "Lokasi" : "Bogor",
}
print("Nama lengkap dari pengguna {0}".format(profile["age"]))


# set Type
f = {1,2,3}
print(f)
g = frozenset({4,5,6,7,8})
print(g)

# TIpe data kondisi Boolean
# boolean isinya cuman 2 : True(1) atau False(0)
value = bool(1)
value = True
print(value)


#binary 
i  = 0b0100001 #binary
# desimal = int(i)
# char = chr(desimal)
# print(char)
print(chr(int(i)))
j = bytearray(a)
print(j)
k = memoryview(j)
print(k)