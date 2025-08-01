import numpy as np
import matplotlib.pyplot as plt

# Load the image
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")

# Separate RGB channels
r = img1[:, :, 0]  # Red channel
g = img1[:, :, 1]  # Green channel
b = img1[:, :, 2]  # Blue channel

# Prepare images and titles for display
output = [img1, r, g, b]
titles = ['Image', 'Red', 'Green', 'Blue']

# Display original image and individual channels
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.axis('off')
    plt.title(titles[i])
    if i == 0:
        plt.imshow(output[i])
    else:
        plt.imshow(output[i], cmap='gray')

plt.show()

# Recombine channels to reconstruct the image
reconstructed = np.dstack((r, g, b))
plt.imshow(reconstructed)
plt.title("Reconstructed Image")
plt.axis('off')
plt.show()
