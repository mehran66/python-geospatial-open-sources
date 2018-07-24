#https://mapbox.github.io/rasterio/quickstart.html
import rasterio
import os
import numpy as np
import matplotlib.pyplot as plt


# Set the current workspace
direc = r"C:\Users\David\Google Drive\OpenSources\data"
os.chdir(direc)
image_file = 'manhattan.tif'

source = rasterio.open(image_file, 'r') 
print(source.count, source.shape)
print(source.width, source.height)
print(source.driver)
print(source.crs)

# Get data from each band (newer versions of rasterio use source.read())
r, g, b = map(source.read_band, (1, 2, 3))
data = np.dstack((r, g, b))  # Each band is just an ndarray!
print(type(data))

# Get the bounds of the raster (for plotting later)
bounds = source.bounds[::2] + source.bounds[1::2]
fig = plt.figure(figsize=(8, 8))
ax = plt.imshow(data, extent=bounds)
plt.show()











