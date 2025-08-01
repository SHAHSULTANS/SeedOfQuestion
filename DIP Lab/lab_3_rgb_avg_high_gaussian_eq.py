import numpy as np
import matplotlib.pyplot as plt
from skimage import io, exposure, img_as_float, img_as_ubyte
from scipy.ndimage import uniform_filter, gaussian_filter, laplace

# Load RGB image
image_path = r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff"
image = io.imread(image_path)
image = img_as_float(image)

# Split channels
R, G, B = image[:, :, 0], image[:, :, 1], image[:, :, 2]

# Define filtering functions
def apply_filters(channel):
    eq = exposure.equalize_hist(channel)
    avg = uniform_filter(channel, size=3)
    gauss = gaussian_filter(channel, sigma=1)
    high = channel - laplace(channel)
    return eq, avg, gauss, high

# Apply filters to each channel
R_eq, R_avg, R_gauss, R_high = apply_filters(R)
G_eq, G_avg, G_gauss, G_high = apply_filters(G)
B_eq, B_avg, B_gauss, B_high = apply_filters(B)

# Reconstruct RGB images
def stack_channels(r, g, b):
    return np.clip(np.stack([r, g, b], axis=-1), 0, 1)

image_eq = stack_channels(R_eq, G_eq, B_eq)
image_avg = stack_channels(R_avg, G_avg, B_avg)
image_gauss = stack_channels(R_gauss, G_gauss, B_gauss)
image_high = stack_channels(R_high, G_high, B_high)

# Image set
titles = ["Original", "Equalized", "Average Filter", "Gaussian Filter", "High-Pass"]
images = [image, image_eq, image_avg, image_gauss, image_high]

# Plot images and histograms
fig, axes = plt.subplots(2, 5, figsize=(25, 10))

for i in range(5):
    # Display image
    axes[0, i].imshow(images[i])
    axes[0, i].set_title(titles[i])
    axes[0, i].axis('off')

    # Display histogram (on RGB channels separately)
    clipped = np.clip(images[i], 0, 1)
    axes[1, i].hist(img_as_ubyte(clipped[:, :, 0]).ravel(), bins=256, color='r', alpha=0.5, label='R')
    axes[1, i].hist(img_as_ubyte(clipped[:, :, 1]).ravel(), bins=256, color='g', alpha=0.5, label='G')
    axes[1, i].hist(img_as_ubyte(clipped[:, :, 2]).ravel(), bins=256, color='b', alpha=0.5, label='B')
    axes[1, i].set_title(f"{titles[i]} Histogram")
    axes[1, i].set_xlabel("Intensity")
    axes[1, i].set_ylabel("Frequency")
    axes[1, i].legend()

plt.tight_layout()
plt.show()
