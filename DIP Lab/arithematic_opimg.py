import numpy as np
import matplotlib.pyplot as plt

# Load two images of the same resolution
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.06.tiff")
img2 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")

# Show individual images
plt.imshow(img1)
plt.title("Image 1")
plt.axis('off')
plt.show()

plt.imshow(img2)
plt.title("Image 2")
plt.axis('off')
plt.show()

# Arithmetic operations
plt.imshow(img1 + img2)  # Addition
plt.title("img1 + img2")
plt.axis('off')
plt.show()

plt.imshow(img1 - img2)  # Subtraction
plt.title("img1 - img2")
plt.axis('off')
plt.show()

plt.imshow(img2 - img1)  # Reverse subtraction
plt.title("img2 - img1")
plt.axis('off')
plt.show()

# Flipping operations
plt.imshow(np.flip(img1, axis=0))  # Flip vertically
plt.title("Vertical Flip (axis=0)")
plt.axis('off')
plt.show()

plt.imshow(np.flip(img1, axis=1))  # Flip horizontally
plt.title("Horizontal Flip (axis=1)")
plt.axis('off')
plt.show()

# Rolling (shifting) image content
plt.imshow(np.roll(img1, shift=2048))
plt.title("Rolled Image (2048 pixels)")
plt.axis('off')
plt.show()

# Flip left to right
plt.imshow(np.fliplr(img1))
plt.title("Flip Left to Right")
plt.axis('off')
plt.show()

# Flip up to down
plt.imshow(np.flipud(img1))
plt.title("Flip Up to Down")
plt.axis('off')
plt.show()

# Rotate 90 degrees
plt.imshow(np.rot90(img1))
plt.title("Rotated 90°")
plt.axis('off')
plt.show()
