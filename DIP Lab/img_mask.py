import numpy as np
import matplotlib.pyplot as plt

# Load the image and create a writable copy
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff").copy()

# Get image dimensions
nrows, ncols, channels = img1.shape

# Create coordinate grids
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols / 2

# Generate outer disk mask
outer_disk_mask = ((row - cnt_row) ** 2 + (col - cnt_col) ** 2 > (nrows / 2) ** 2)

# Apply mask: set pixels outside the central disk to black
img1[outer_disk_mask] = 0

# Show the masked image
plt.imshow(img1)
plt.axis('off')
plt.title('Masked Image')
plt.show()
