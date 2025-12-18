import numpy as np
import matplotlib.pyplot as plt
row = 1080*2
col = 1080*2

x1 = 300; y1 = 700
x2 = 700; y2 = 700
x3= 300; y3= 400
x4 = 700; y4= 400
x5 = int((x2 + x3) / 2); y5= int(400/2)
warna = (0, 50, 255)
warna_garis = warna
width = 20
lw = 10
# px = 200, py = 400
r = 20
# make dot
def titik(img, py,px, r, warna):
    for y in range (py-r, py+r+1):
        for x in range(px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                img[y,x] = warna
# garis
def garis(img, y1,x1, y2, x2, lw, warna_garis):
    r = round(lw/2)
    no_of_dots = max(abs(x2-x1), abs(y2-y1))
    if abs(x2-x1) > abs(y2-y1):
        m = abs(y2-y1) / abs(x2-x1)
        x = x1
        dx = 1
        y = y1
        dy = m * dx 
        for i in range(0, no_of_dots):
            x += dx
            y += dy
            x_int = round(x)
            y_int  = round(y)
            px = x_int
            py = y_int
            titik(img, py,px, r, warna_garis)
    if abs(x2-x1) < abs(y2-y1):
        m = abs(x2-x1) / abs(y2-y1)
        y = y1
        dx = 1
        x = x1
        dy = m * dx 
        for i in range(0, no_of_dots):
            x += dx
            y += dy
            x_int = round(x)
            y_int  = round(y)
            px = x_int
            py = y_int
            titik(img, py,px, r, warna_garis)
# program
img = np.zeros(shape=(row,col,3), dtype = np.uint8)
px = x1; py = y1
titik(img,py,px,r,warna)
plt.imshow(img)
plt.show()
px = x2; py = y2
titik(img,py,px,r,warna)
plt.imshow(img)
plt.show()
px = x3; py = y3
titik(img,py,px,r,warna)
px = x4; py = y4
titik(img,py,px,r,warna)
px = x5; py = y5
titik(img,py,px,r,warna)
garis(img, y1,x1, y2, x2, lw, warna)
garis(img, y3,x3, y2, x2, lw, warna)
garis(img, y3,x3, y4, x4, lw, warna)
garis(img, y1,x1, 400, x4, lw, warna)

plt.imshow(img)
plt.show()



