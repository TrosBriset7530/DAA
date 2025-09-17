import datetime
#1
aList = ["John", 33, "Toronto", True]
print(aList)
#Date and Mahasiswa
x = datetime.date.today()
date = x.strftime("%d-%m-%Y")
mahasiswa = ["Rafael Octo", 2024071003, "Informatika", "DAA", date, "Universitas Pembangunan Jaya"]
print(mahasiswa)
print(mahasiswa[1]) # NIM

#Slicing
print('')
print(mahasiswa[1:3])
#Iterasi
for i in mahasiswa:
    print(i, "UPJ")
#Tuple
print('')
upj = ('Universitas', 'pembangunan jaya')
print(upj)
#Nested Tuple
nested_tuple = (100, (200,400,600), 300, (400,800))
print(nested_tuple) #200
#Dictionary
bin_Colors = {
    "nama" : "Rafael Octo",
    "NIM" : 2024071003,
    "Prodi" : "Informatika",
    "Universitas" : "UPJ",
}
print(bin_Colors)
#Sets
print('')
red = {'blood', 'rose', 'fire hydrant', 'leaves'}
yellow = {'dandelion', 'fire hydrant', 'leaves'}
print(red|yellow) #union
print(red&yellow) #intersection