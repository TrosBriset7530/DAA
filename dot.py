import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')
fig = plt.figure(figsize=(10.8, 10.8), dpi=100)
x1, y1 = np.array([240, 480]), np.array([240, 240])
x2, y2 = np.array([240, 480]), np.array([480, 480])
x3, y3 = np.array([240, 240]), np.array([240, 480])
x4, y4 = np.array([480, 480]), np.array([240, 480])
x5, y5 = np.array([240, 480]), np.array([480, 480])
x6, y6 = np.array([360, 240]), np.array([620, 480])
x7, y7 = np.array([360, 480]), np.array([620, 480])
x8, y8 = np.array([240, 480]), np.array([240, 480])
x9, y9 = np.array([240, 480]), np.array([480, 240])
plt.plot(x1, y1, x2, y2, marker = 'o', color="blue")
plt.plot(x3, y3, x4, y4, marker = 'o', color="blue")
plt.plot(x6, y6, x7 ,y7, x8, y8, x9, y9, marker = 'o', color="blue")

plt.savefig('plot_1080.png', dpi = 300, bbox_inches='tight')
plt.show()
# plt.savefig("my.jpg", format='jpeg', dpi=1080)

