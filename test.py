def str(z,y):
    x = ""
    for i in z:
        x += i
        if i == ' ':
            x = ""
        if x == y:
            return True
    return False
# def bin(z,y):
#     for i in range(0,len(z)):

pattern = "True"
teks = "nobody noticed him"
bin1 = "001011"
bin2 = "10010101001011110101010001"
bin3 = ""
for i in range(0, len(bin2) - len(bin1) + 1):
    for j in range(i, len(bin1)+i):
        bin3 += bin2[j]
        if(bin3 == bin1):
            print(True)
            break
    bin3 = ""
print(str(teks,pattern))


