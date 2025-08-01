import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread(r"C:\Users\ACER\Desktop\4_1 CSE JU\misc\4.1.04.tiff")
img = img.astype(np.float32) / 255


R = img[:, :, 0]
G = img[:, :, 1]
B = img[:, :, 2]

I = (R + G + B) / 3


min_rgb = np.minimum(np.minimum(R, G), B)
S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb


numerator = 0.5 * ((R - G) + (R - B))
denominator = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6
theta = np.arccos(np.clip(numerator / denominator, -1, 1))
H = np.where(B > G, 2 * np.pi - theta, theta)
H = H / (2 * np.pi)


HSI = np.stack((H, S, I), axis=2)

plt.figure(figsize=(12,6))
plt.subplot(1, 4, 1)
plt.imshow(HSI)
plt.title('HSI Image')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(H, cmap='hsv')
plt.title('Hue')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(S, cmap='gray')
plt.title('Saturation')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(I, cmap='gray')
plt.title('Intensity')
plt.axis('off')

plt.tight_layout()
plt.show()


I_8bit = (I * 255).astype(np.uint8)


plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(I_8bit.flatten(), bins=256, range=[0,256], color='gray')
plt.title('Original Intensity Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

hist, bins = np.histogram(I_8bit.flatten(), bins=256, range=[0,256])
cdf = hist.cumsum()
cdf_min = cdf[np.nonzero(cdf)].min()
cdf_eq = (cdf - cdf_min) * 255 / (cdf.max() - cdf_min)
cdf_eq = np.clip(cdf_eq, 0, 255).astype(np.uint8)

I_eq = cdf_eq[I_8bit]


plt.subplot(1, 2, 2)
plt.hist(I_eq.flatten(), bins=256, range=[0,256], color='gray')
plt.title('Equalized Intensity Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(I, cmap='gray')
plt.title('Original Intensity')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(I_eq, cmap='gray')
plt.title('Equalized Intensity')
plt.axis('off')

plt.tight_layout()
plt.show()





I = I_eq.astype(np.float32) / 255 


H = H * 2 * np.pi  
S = np.clip(S, 0, 1)
I = np.clip(I, 0, 1)

R_new = np.zeros_like(I)
G_new = np.zeros_like(I)
B_new = np.zeros_like(I)


idx1 = (H >= 0) & (H < 2*np.pi/3)
B_new[idx1] = I[idx1]*(1 - S[idx1])
R_new[idx1] = I[idx1]*(1 + S[idx1]*np.cos(H[idx1]) / np.cos(np.pi/3 - H[idx1]))
G_new[idx1] = 3*I[idx1] - (R_new[idx1] + B_new[idx1])


idx2 = (H >= 2*np.pi/3) & (H < 4*np.pi/3)
H2 = H[idx2] - 2*np.pi/3
R_new[idx2] = I[idx2]*(1 - S[idx2])
G_new[idx2] = I[idx2]*(1 + S[idx2]*np.cos(H2) / np.cos(np.pi/3 - H2))
B_new[idx2] = 3*I[idx2] - (R_new[idx2] + G_new[idx2])


idx3 = (H >= 4*np.pi/3) & (H <= 2*np.pi)
H3 = H[idx3] - 4*np.pi/3
G_new[idx3] = I[idx3]*(1 - S[idx3])
B_new[idx3] = I[idx3]*(1 + S[idx3]*np.cos(H3) / np.cos(np.pi/3 - H3))
R_new[idx3] = 3*I[idx3] - (G_new[idx3] + B_new[idx3])


RGB_reconstructed = np.stack((R_new, G_new, B_new), axis=2)
RGB_reconstructed = np.clip(RGB_reconstructed, 0, 1)


plt.figure(figsize=(6,6))
plt.imshow(RGB_reconstructed)
plt.title('Reconstructed RGB from HSI')
plt.axis('off')
plt.show()
