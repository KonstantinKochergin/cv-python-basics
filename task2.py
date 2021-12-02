import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label

im1 = np.loadtxt("img1.txt", skiprows=2)
im2 = np.loadtxt("img2.txt", skiprows=2)

im1Region = regionprops(label(im1))[0]
im2Region = regionprops(label(im2))[0]
im1X = im1Region.coords[0][1]
im1Y = im1Region.coords[0][0]
im2X = im2Region.coords[0][1]
im2Y = im2Region.coords[0][0] 

print(f"offset X: {abs(im1X - im2X)} Y: {abs(im1Y - im2Y)}")
