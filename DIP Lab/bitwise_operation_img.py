import numpy as np
import matplotlib.pyplot as plt

# Load images with same shape and type
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.06.tiff").astype(np.uint8)
img2 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff").astype(np.uint8)

# Bitwise AND
plt.imshow(np.bitwise_and(img1, img2))
plt.title("Bitwise AND")
plt.axis('off')
plt.show()

# Bitwise OR
plt.imshow(np.bitwise_or(img1, img2))
plt.title("Bitwise OR")
plt.axis('off')
plt.show()

# Bitwise XOR
plt.imshow(np.bitwise_xor(img1, img2))
plt.title("Bitwise XOR")
plt.axis('off')
plt.show()

# Bitwise NOT (image inversion)
plt.subplot(1, 2, 1)
plt.imshow(img1)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(np.bitwise_not(img1))
plt.title("Bitwise NOT (Inverted)")
plt.axis('off')

plt.show()
