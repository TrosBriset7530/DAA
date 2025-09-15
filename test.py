import datetime
#1
aList = ["John", 33, "Toronto", True]
print(aList)
#2
x = datetime.date.today()
date = x.strftime("%d-%m-%Y")
mahasiswa = ["Rafael Octo", 2024071003, "Informatika", "DAA", date, "Universitas Pembangunan Jaya"]
for i in mahasiswa:
    print(i)