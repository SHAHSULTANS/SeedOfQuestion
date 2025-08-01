import numpy as np
import matplotlib.pyplot as plt

# Load the color image
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.01.tiff")

# Separate RGB channels
r = img1[:, :, 0]
g = img1[:, :, 1]
b = img1[:, :, 2]

# Set up subplots with spacing
plt.subplots_adjust(hspace=0.5, wspace=0.5)

# Display the original image
plt.subplot(2, 2, 1)
plt.title('Original Image')
plt.axis('off')
plt.imshow(img1)

# Red channel histogram
hist_r, bins_r = np.histogram(r.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 2)
plt.title('Red Histogram')
plt.bar(bins_r[:-1], hist_r, color='red')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

# Green channel histogram
hist_g, bins_g = np.histogram(g.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 3)
plt.title('Green Histogram')
plt.bar(bins_g[:-1], hist_g, color='green')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

# Blue channel histogram
hist_b, bins_b = np.histogram(b.ravel(), bins=256, range=(0, 256))
plt.subplot(2, 2, 4)
plt.title('Blue Histogram')
plt.bar(bins_b[:-1], hist_b, color='blue')
plt.xlabel('Intensity')
plt.ylabel('Frequency')

plt.show()
