import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy.ndimage import gaussian_filter


img = mpimg.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")
if img.ndim == 3:
    img_gray = img.mean(axis=2) 
else:
    img_gray = img  


blur1 = gaussian_filter(img_gray, sigma=1)
blur3 = gaussian_filter(img_gray, sigma=3)


plt.figure(figsize=(15,5))

plt.subplot(1, 3, 1)
plt.imshow(img_gray, cmap='gray')
plt.title('Original Grayscale')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(blur1, cmap='gray')
plt.title('Blurred (σ = 1)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(blur3, cmap='gray')
plt.title('Blurred (σ = 3)')
plt.axis('off')

plt.tight_layout()
plt.show()
