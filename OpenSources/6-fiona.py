import fiona
import os
import numpy as np

# Set the current workspace
direc = r"C:\Users\David\Google Drive\OpenSources\data\nybb"
os.chdir(direc)

boro_file = "nybb.shp"
# Open the shapefile (can also open directly from zip files with vfs!)
source = fiona.open(boro_file) 
print("Feature Count: %s" % len(source))
print("Input Driver: %s" % source.driver)
source.crs
meta = source.meta
source.schema
feature = source.next()
feature.keys()
feature['geometry']
feature['properties']

