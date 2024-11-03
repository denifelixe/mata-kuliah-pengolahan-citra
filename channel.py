
#pip install numpy
import numpy as np
import imageio as img
import matplotlib.pyplot as plt

# Load Gambar
image = img.imread("D:/source.jpg")

# Channel Warna
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

# Menambahkan citra/gambar untuk channel Merah Hijau Biru
imgRed = np.zeros_like(image)
imgRed[:,:,0] = red

imgGreen = np.zeros_like(image)
imgGreen[:,:,1] = green

imgBlue = np.zeros_like(image)
imgBlue[:,:,2] = blue

# Plot channel warna
plt.figure(figsize=(10,10))
plt.subplot(4,1,1)
plt.imshow(image)
plt.title("Original Image")

plt.subplot(4,1,2)
plt.imshow(imgRed)
plt.title("Red Channel")

plt.subplot(4,1,3)
plt.imshow(imgGreen)
plt.title("Green Channel")

plt.subplot(4,1,4)
plt.imshow(imgBlue)
plt.title("Blue Channel")

plt.tight_layout()
plt.show()
