'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Purpose: Access raster file and convert to numpy array
*********************************************'''

import os
from osgeo import gdal,gdalnumeric
import numpy as np

path = r'D:\data'
os.chdir(path)
os.listdir(path)

#input variables
l5 = 'L5034032_2001_B3.tif'
outName = 'myOutput.tif'
out_dtype = gdal.GDT_Byte

#open the raster file with gdal
g = gdal.Open(l5)
#get the projection object
prj = g.GetProjection()
#get properites from the gdal object
cols = g.RasterXSize
rows = g.RasterYSize
#get the band object from the gdal object
bnd = g.GetRasterBand(1)
#use the band object to create a numpy array
npArray = bnd.ReadAsArray()
print 'File read as np array'

#or there is a shortcut
npArray2 = gdalnumeric.LoadFile(l5)

#do some analysis in numpy

#write the output back to a raster file format
driver = g.GetDriver()
#driver = gdal.GetDriverByName('GTiff')
driver.Register()

outFile = driver.Create(outName,npArray.shape[1],npArray.shape[0],1,out_dtype)
outFile.GetRasterBand(1).WriteArray(npArray,0,0)
outFile.GetRasterBand(1).ComputeStatistics(False)

outFile = None
print 'File written to disk'