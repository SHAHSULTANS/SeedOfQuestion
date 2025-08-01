import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color, exposure, img_as_float
from scipy.ndimage import uniform_filter, gaussian_filter, laplace
from skimage.util import img_as_ubyte

# Load and convert to grayscale
image_path = r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff"
image = io.imread(image_path)
gray = color.rgb2gray(image)
gray = img_as_float(gray)

# Apply filters
equalized = exposure.equalize_hist(gray)
average_filtered = uniform_filter(gray, size=3)
gaussian_filtered = gaussian_filter(gray, sigma=1)
high_pass = gray - laplace(gray)

# Clip all images to [0, 1] before histogram conversion
images = [gray, equalized, average_filtered, gaussian_filtered, high_pass]
titles = ["Original", "Equalized", "Average Filter", "Gaussian Filter", "High-Pass"]

# Display images and histograms
fig, axes = plt.subplots(2, 5, figsize=(25, 8))

for i in range(5):
    # Top row: images
    axes[0, i].imshow(images[i], cmap='gray')
    axes[0, i].set_title(titles[i])
    axes[0, i].axis('off')

    # Bottom row: histograms
    safe_image = np.clip(images[i], 0, 1)
    axes[1, i].hist(img_as_ubyte(safe_image).ravel(), bins=256, range=[0, 256], color='gray')
    axes[1, i].set_title(f"{titles[i]} Histogram")
    axes[1, i].set_xlabel("Intensity")
    axes[1, i].set_ylabel("Frequency")

plt.tight_layout()
plt.show()
