import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label

files = ["figure1.txt", "figure2.txt", "figure3.txt", "figure4.txt", "figure5.txt", "figure6.txt"]
for file in files:
    f = open(file, 'r')
    horInMm = float(f.readline())
    f.close()
    im = np.loadtxt(file, skiprows=2)
    regions = regionprops(label(im))
    if (len(regions) == 1):
        print(f"Resolution for {file} = {horInMm / regions[0].image.shape[1]}")
    else:
        print("Empty image")

    