import os
from osgeo import ogr
from osgeo import gdal


path = r'C:\Users\David\Desktop\testdata\n39w107'
#change the working directory
os.chdir(path)

filename = 'grdn39w107_13\w001001.adf'

#Register all drivers at once
gdal.AllRegister()

# Open the file:
dataset = gdal.Open(filename)
if ds is None:
	print 'Could not open ' + fn
	sys.exit(1)
	
#Getting image dimensions
cols = dataset.RasterXSize
rows = dataset.RasterYSize
bands = dataset.RasterCount
driver = dataset.GetDriver().LongName #ArcInfo ESRI grid



src_proj = dataset.GetProjection()


src_geotrans = dataset.GetGeoTransform()    
"""
	adfGeoTransform[0] /* top left x */
    adfGeoTransform[1] /* w-e pixel resolution */
    adfGeoTransform[2] /* rotation, 0 if image is "north up" */
    adfGeoTransform[3] /* top left y */
    adfGeoTransform[4] /* rotation, 0 if image is "north up" */
    adfGeoTransform[5] /* n-s pixel resolution */ 
"""
originX = geotransform[0]
originY = geotransform[3]
pixelWidth = geotransform[1]
pixelHeight = geotransform[5]

xOffset = int((x – originX) / pixelWidth)
yOffset = int((y – originY) / pixelHeight)

#But how to get the individual data values in the file?
band = dataset.GetRasterBand(1)
bandtype = gdal.GetDataTypeName(band.DataType) #'Float32'
scanline = band.ReadRaster( 0, 0, band.XSize, 1,band.XSize, 1, band.DataType)
#So you might say "0,0,512,512,100,100" to read a 512x512 block at the top left of the image into a 100x100 buffer (downsampling the image).
import struct
value = struct.unpack('f' * band.XSize, scanline)
#Now I can get individual values
value[8]


#read the whole file into an array
data = band.ReadAsArray(0, 0, cols, rows)
value = data[3500,4000]
#Using the numpy library I can define the datatype in the array:
import numpy
data = band.ReadAsArray(0, 0, dataset.RasterXSize, dataset.RasterYSize).astype(numpy.float)


#Memory management
band = None
dataset = None



#***********************************************************
#Script example 1

# script to get pixel values at a set of coordinates
# by reading in one pixel at a time
# Took 0.47 seconds on my machine
import os, sys, time, gdal
from gdalconst import *
# start timing
startTime = time.time()
# coordinates to get pixel values for
OS Python week 4: Reading raster data [17]
xValues = [447520.0, 432524.0, 451503.0]
yValues = [4631976.0, 4608827.0, 4648114.0]
# set directory
os.chdir(r'Z:\Data\Classes\Python\data')
# register all of the drivers
gdal.AllRegister()
# open the image
ds = gdal.Open('aster.img', GA_ReadOnly)
if ds is None:
print 'Could not open image'
sys.exit(1)


# get image size
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount
# get georeference info
transform = ds.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
# loop through the coordinates
OS Python week 4: Reading raster data [18]
for i in range(3):
	# get x,y
	x = xValues[i]
	y = yValues[i]
	# compute pixel offset
	xOffset = int((x - xOrigin) / pixelWidth)
	yOffset = int((y - yOrigin) / pixelHeight)
	# create a string to print out
	s = str(x) + ' ' + str(y) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' '
	# loop through the bands
	for j in range(bands):
		band = ds.GetRasterBand(j+1) # 1-based index
		# read data and add the value to the string
		data = band.ReadAsArray(xOffset, yOffset, 1, 1)
		value = data[0,0]
		s = s + str(value) + ' ‘
	# print out the data string
	print s
# figure out how long the script took to run
endTime = time.time()
print 'The script took ' + str(endTime - startTime) + ' seconds'


#Script example 2
# script to get pixel values at a set of coordinates
# by reading in entire bands
# Took 1.69 seconds on my machine
import os, sys, time, gdal
from gdalconst import *
# start timing
startTime = time.time()
# coordinates to get pixel values for
OS Python week 4: Reading raster data [20]
xValues = [447520.0, 432524.0, 451503.0]
yValues = [4631976.0, 4608827.0, 4648114.0]
# set directory
os.chdir(r'Z:\Data\Classes\Python\data')
# register all of the drivers
gdal.AllRegister()
# open the image
ds = gdal.Open('aster.img', GA_ReadOnly)
if ds is None:
	print 'Could not open image'
	sys.exit(1)

# get image size
rows = ds.RasterYSize
cols = ds.RasterXSize
bands = ds.RasterCount
# get georeference info
transform = ds.GetGeoTransform()
xOrigin = transform[0]
yOrigin = transform[3]
pixelWidth = transform[1]
pixelHeight = transform[5]
# create a list to store band data in
OS Python week 4: Reading raster data [21]
bandList = []
# read in bands and store all the data in bandList
for i in range(bands):
	band = ds.GetRasterBand(i+1)
	data = band.ReadAsArray(0, 0, cols, rows)
	bandList.append(data)
	# loop through the coordinates
for i in range(3):
	# get x,y
	x = xValues[i]
	y = yValues[i]
	# compute pixel offset
	xOffset = int((x - xOrigin) / pixelWidth)
	yOffset = int((y - yOrigin) / pixelHeight)
	# create a string to print out
	s = str(x) + ' ' + str(y) + ' ' + str(xOffset) + ' ' + str(yOffset) + ' ‘
	# loop through the bands and get the pixel value
		for j in range(bands):
		data = bandList[j]
		value = data[yOffset, xOffset] # math matrix notation order
		s = s + str(value) + ' ‘
		# print out the data string
		OS Python week 4: Reading raster data [22]
	print s
# figure out how long the script took to run
endTime = time.time()
print 'The script took ' + str(endTime - startTime) + ' seconds'


	
