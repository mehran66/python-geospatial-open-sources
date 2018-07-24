'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Purpose: Access raster file and convert to numpy array
#http://pcjericks.github.io/py-gdalogr-cookbook/index.html
*********************************************'''

import os
from osgeo import gdal,gdalnumeric
import numpy as np

# Set the current workspace
direc = r"C:\Users\David\Google Drive\OpenSources\data"
os.chdir(direc)

#input variables
l5 = 'L5034032_2001_B3.tif'
outName = 'myOutput.tif'

#open the raster file with gdal
g = gdal.Open(l5)
#get the projection object
prj = g.GetProjection()
#get properites from the gdal object
cols = g.RasterXSize
rows = g.RasterYSize
#get the band object from the gdal object
bnd = g.GetRasterBand(1)

#Getting georeference info
src_geotrans = g.GetGeoTransform()    
"""
	adfGeoTransform[0] /* top left x */
    adfGeoTransform[1] /* w-e pixel resolution */
    adfGeoTransform[2] /* rotation, 0 if image is "north up" */
    adfGeoTransform[3] /* top left y */
    adfGeoTransform[4] /* rotation, 0 if image is "north up" */
    adfGeoTransform[5] /* n-s pixel resolution */ 
"""


#use the band object to create a numpy array
npArray = bnd.ReadAsArray()
print 'File read as np array'

#or there is a shortcut
npArray2 = gdalnumeric.LoadFile(l5)

#do some analysis in numpy

#write the output back to a raster file format
driver = g.GetDriver() #A driver is an object that knows how to interact with a certain data type
#driver = gdal.GetDriverByName('GTiff')
driver.Register()
out_dtype = gdal.GDT_Byte # unsigned 8 bit integer (values from 0-255)

outFile = driver.Create(outName,npArray.shape[1],npArray.shape[0],1,out_dtype) # the '1' is for band 1.
outFile.GetRasterBand(1).WriteArray(npArray)
outFile.GetRasterBand(1).ComputeStatistics(False)
print 'File written to disk'