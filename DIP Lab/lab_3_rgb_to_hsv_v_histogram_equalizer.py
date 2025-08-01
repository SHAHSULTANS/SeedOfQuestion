import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_ubyte

# Load image
image_path = r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.02.tiff"
image = io.imread(image_path)

# Extract channels
R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]

# Convert to HSV and get V
image_hsv = color.rgb2hsv(image)
V = image_hsv[:, :, 2]

# Equalize V and convert back to RGB
V_eq = exposure.equalize_hist(V)
image_hsv[:, :, 2] = V_eq
image_eq = color.hsv2rgb(image_hsv)

# Prepare display
fig, axes = plt.subplots(2, 5, figsize=(25, 8))
titles = ["Original Image", "R Channel", "G Channel", "B Channel", "V Equalized"]
images = [image, R, G, B, image_eq]
cmaps = [None, 'Reds', 'Greens', 'Blues', None]
channels = [img_as_ubyte(V), R, G, B, img_as_ubyte(V_eq)]
colors = ['purple', 'red', 'green', 'blue', 'orange']

# First row: images
for i in range(5):
    axes[0, i].imshow(images[i], cmap=cmaps[i])
    axes[0, i].set_title(titles[i])
    axes[0, i].axis('off')

# Second row: histograms
for i in range(5):
    axes[1, i].hist(channels[i].ravel(), bins=256, range=[0, 256], color=colors[i])
    axes[1, i].set_title(f"{titles[i]} Histogram")
    axes[1, i].set_xlabel("Intensity")
    axes[1, i].set_ylabel("Frequency")

plt.tight_layout()
plt.show()
