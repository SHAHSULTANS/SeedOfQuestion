import matplotlib.pyplot as plt

# Load the image
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")

# Explore properties
print(type(img1))      # Shows it's a NumPy ndarray
print(img1.shape)      # (height, width, channels) for color image
print(img1.ndim)       # Number of dimensions (should be 3 for color image)
print(img1.size)       # Total number of elements = height × width × channels
print(img1.dtype)      # Data type of individual pixels (often float32 or uint8)
print(img1.nbytes)     # Total memory consumed by the image (in bytes)
