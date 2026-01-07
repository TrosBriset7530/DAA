# Delta Algorithm for Creating a Line
# You can use and modify it but retain this attribution.
# Mohammad Nasucha, Ph.D.
# Students can learn that this algorithm is simpler (does not
# use conditions) yet robust in anticipating verticality, 
# horizontality, and reversed order of the two points.  

print("\033c")       
import numpy as np
import matplotlib.pyplot as plt

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++              USER ENTRIES           +++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
row, col = 1080, 1080
lw = 5
line_color = [255,0,0]
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++        MEMBUAT GARIS DENGAN METODE INCREMENT (DELTA x dan DELTA y)  +++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def buat_garis(gambar, y1, x1, y2, x2, lw, line_color):
    hw = round(lw)                                                   #line half width
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
        # Untuk animasi garis
        if round(x) == round(x2) and round(y) == round(y2):
            image.set_data(gambar)
            plt.pause(0.5) 
    return gambar
# Titik
def titik(img, py,px, r, warna):
    for y in range (py-r, py+r+1):
        for x in range(px-r, px+r+1):
            if (y-py)**2 + (x-px)**2 <= r**2:
                img[y,x] = warna
    return img
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++           MAIN PROGRAM          ++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# plt.ion()
plt.show(block=False)
plt.figure()

print('col, row =', col, ',', row)
# preparing the black canvas
gambar = np.zeros(shape=(round(row), round(col), 3), dtype=np.uint8)

nodes = {
    'bottom':   (930, 540),
    'left':     (540, 250),
    'topLeft':  (350, 400),
    'right':    (540, 830),
    'topRight': (350, 680),
    'center':   (620, 540)
}
# 1. Draw Nodes/Points
for i in nodes.values():
    titik(gambar, i[0], i[1], lw*4, [255,255,255])
plt.imshow(gambar)
plt.show()
# 2. Define lines coordinate as an Array [y1, x1, y2, x2]
lines = np.array([
    [*nodes['bottom'],   *nodes['left']],     # A: Bottom -> Left
    [*nodes['left'],     *nodes['topLeft']],  # B: Left -> TopLeft
    [*nodes['topLeft'],  *nodes['center']],   # C: TopLeft -> Center
    [*nodes['left'],     *nodes['center']],   # D: Left -> Center
    [*nodes['left'],     *nodes['topRight']], # E: Left -> TopRight
    [*nodes['topLeft'],  *nodes['topRight']], # F: TopLeft -> TopRight
    [*nodes['right'],    *nodes['topLeft']],   # G: Right -> TopLeft
    [*nodes['topRight'], *nodes['right']],    # H: TopRight -> Right
    [*nodes['topRight'], *nodes['center']],   # I: TopRight -> Center
    [*nodes['right'],    *nodes['center']],   # J: Right -> Center
    [*nodes['right'],    *nodes['bottom']],   # K: Right -> Bottom
])

# 3. Iterate through the array to draw
for i in lines:
    y1, x1, y2, x2 = i
    hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)
plt.imshow(hasil)
plt.show()


