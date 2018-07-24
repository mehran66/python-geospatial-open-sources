'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Updated: 03/14/2016 , Stefan Leyk
Purpose: Access raster file and convert to numpy array
*********************************************'''

import os
from osgeo import gdal,gdalnumeric
import numpy as np

path = r'C:\GIS3\data\cl08data'
os.chdir(path)
os.listdir(path)

# Define input variables
l5 = r'L5034032_2001_B3.tif'
outName = r'myOut.tif'
out_dtype = gdal.GDT_Byte

# Open the raster file with gdal
g = gdal.Open(l5)
# Get the projection object
prj = g.GetProjection()
# Get properites from the gdal object
cols = g.RasterXSize
rows = g.RasterYSize
# Get the band object from the gdal object
# You could basically get several band and calculate e.g., NDVI
bnd = g.GetRasterBand(1)
# Use the band object to create a numpy array
npArray = bnd.ReadAsArray()
print 'File read as np array'

# or there is a shortcut
npArray2 = gdalnumeric.LoadFile(l5)

# Do some analysis in numpy
npArray = npArray/100

# Write the output back to a raster file format
driver = g.GetDriver()
# Driver = gdal.GetDriverByName('GTiff')
driver.Register()

outFile = driver.Create(outName,npArray.shape[1],npArray.shape[0],1,out_dtype)
outFile.GetRasterBand(1).WriteArray(npArray,0,0)
outFile.GetRasterBand(1).ComputeStatistics(False)

outFile = None
print 'File written to disk'