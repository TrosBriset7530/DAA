import numpy as np
import matplotlib.pyplot as plt

row, col = 1080, 1080
lw = 6
line_color = [255,255,0]

def buat_garis(gambar, y1, x1, y2, x2, lw, line_color):
    hw = round(lw)
    juml_step = max(abs(y2-y1), abs(x2-x1))
    dy = (y2-y1)/juml_step
    dx = (x2-x1)/juml_step
    #Mulai membuat garis.
    y = y1
    x = x1
    image = plt.imshow(gambar)
    for i in range(0, juml_step+1):
        #kumpulan pixel berbentuk kotak:
        gambar[round(y)-hw:round(y)+hw, round(x)-hw:round(x)+hw] = line_color
        y += dy
        x += dx
    return gambar
def titik(img, py,px, r, warna):
    for y in range (py-r, py+r+1):
        for x in range(px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                img[y,x] = warna
    return img
# plt
plt.show(block=False)
plt.figure()
gambar = np.zeros(shape=(round(row), round(col), 3), dtype=np.uint8)

nodes = {
    'center': (round(270+100), 540),
    'left':     (540+100, 380),
    'right':    (540+100, 700)
    }

for i in nodes.values():
    titik(gambar, i[0], i[1], lw*3, [255,255,255])

lines = np.array([
    [*nodes['center'],   *nodes['left']], 
    [*nodes['left'],   *nodes['right']], 
    [*nodes['right'],   *nodes['center']],     
])

# 3. Iterate through the array to draw
for i in lines:
    y1, x1, y2, x2 = i
    gambar = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

plt.imshow(gambar)
plt.show()