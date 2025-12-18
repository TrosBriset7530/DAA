# Delta Algorithm for Creating a Line
# You can use and modify it but retain this attribution.
# Mohammad Nasucha, Ph.D.
# Students can learn that this algorithm is simpler (does not
# use conditions) yet robust in anticipating verticality, 
# horizontality, and reversed order of the two points.  

print("\033c")       #To close('all') all previous terminals.
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
    n = 0
    #Mulai membuat garis.
    y = y1
    x = x1
    image = plt.imshow(gambar)
    for i in range(0, juml_step+1):
        #kumpulan pixel berbentuk kotak:
        gambar[round(y)-hw:round(y)+hw, round(x)-hw:round(x)+hw] = line_color
        y += dy
        x += dx
        n += 1
        if n == 100:
            image.set_data(gambar)
            plt.pause(0.1) 
            n = 0
    return gambar

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++           MAIN PROGRAM          ++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# plt.ion()
plt.show(block=False)
plt.figure()

print('col, row =', col, ',', row)
# preparing the black canvas
gambar = np.zeros(shape=(round(row), round(col), 3), dtype=np.uint8)

# Coordinates from Table (Mapped as y, x)
# Paling Atas: (150, 540)
# Atas Tengah Kanan: (350, 680)
# Tengah Paling Kanan: (540, 830)
# Bawah Tengah Kanan: (730, 680)
# Paling Bawah: (930, 540)
# Bawah Tengah Kiri: (730, 400)
# Tengah Paling Kiri: (540, 250)
# Atas Tengah Kiri: (350, 400)

# 1. Top to Upper Right
y1, x1 = 150, 540
y2, x2 = 350, 680
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 2. Upper Right to Mid Right
y1, x1 = 350, 680
y2, x2 = 540, 830
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 3. Mid Right to Low Right
y1, x1 = 540, 830
y2, x2 = 730, 680
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 4. Low Right to Bottom
y1, x1 = 730, 680
y2, x2 = 930, 540
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 5. Bottom to Low Left
y1, x1 = 930, 540
y2, x2 = 730, 400
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 6. Low Left to Mid Left
y1, x1 = 730, 400
y2, x2 = 540, 250
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

# 7. Mid Left to Upper Left
y1, x1 = 540, 250
y2, x2 = 350, 400
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

y1, x1 = 540, 250
y2, x2 = 350, 400
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)


# 8. Upper Left to Top (Closing the loop)
y1, x1 = 350, 400
y2, x2 = 150, 540
hasil = buat_garis(gambar, y1, x1, y2, x2, lw, line_color)

plt.imshow(hasil)
plt.show()


