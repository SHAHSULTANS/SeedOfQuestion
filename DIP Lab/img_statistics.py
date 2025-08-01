import numpy as np
import matplotlib.pyplot as plt

# Load the image
img1 = plt.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")

# Basic image statistics
print("Min value:", img1.min())
print("Max value:", img1.max())
print("Mean value:", img1.mean())

# Additional NumPy statistical functions
print("Median value:", np.median(img1))
print("Average value:", np.average(img1))
print("Mean (again):", np.mean(img1))
print("Standard deviation:", np.std(img1))
print("Variance:", np.var(img1))
