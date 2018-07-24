'''*********************************************
author: Galen Maclaurin
Date: 3/17/2014
Purpose: Square buffer example
*********************************************'''

from time import clock
start = clock()
import os
from osgeo import ogr

path = r'/media/ALENIO16GB/GEOG4303/GDAL/data'
#change the working directory
os.chdir(path)
theme = 'boulder_sites.shp'
buffTheme = 'squareBuff.shp'
buffDist = 2000

#open the feature class, creating an ogr object
ds = ogr.Open(theme)
#get the driver from the ogr object. The driver object is an interface to work
#with a specific vector data format (i.e. ESRI shapefile in this case).
dvr = ds.GetDriver()
#check to see if the output file exists and delete it if so.
if os.path.exists(buffTheme):
    dvr.DeleteDataSource(buffTheme)

#get the layer object from the ogr object. This is kind of like a cursor object.
lyr = ds.GetLayer()
#get the number of features. the layer object is an iterable object.
numFeat = len(lyr)

#create an empty feature class to populate with buffer features. This is stored
#in memory as an emtpy ogr object.
buff_ds = dvr.CreateDataSource(buffTheme)
#create a layer object from the empty ogr object.
outLyr = buff_ds.CreateLayer(buffTheme[:-4],lyr.GetSpatialRef(),\
ogr.wkbPolygon)
#use a layer definition to create a feature
lyrDef = outLyr.GetLayerDefn()

#create a ring geometry object, this is like an array specifically for a polygon
#**************
#create a polygon geometry object
#**************
#iterate through the features in the layer object (like with a cursor)
for feat in lyr:
    #get the geometry object from the feature object.
    geom = feat.GetGeometryRef()
    #buffer the feature
    buff = geom.Buffer(buffDist)
    #get the envelope of the buffer, i.e. the coordinates of the square buffer
    #**************
    #populate the ring
    #**************
    #add the ring to the polygon
    #**************
    #create a new feature using the layer definition create outside the loop
    outFeat = ogr.Feature(lyrDef)
    #set the feature's geometry as the buffered geometry
    outFeat.SetGeometry(*****)
    #save the new feature in the output layer created outside the loop
    outLyr.CreateFeature(outFeat)
    #empty the ring and polygon objects
    #**************
    #**************
#clean up, remove reference to the datasource objects, this is like deleting
#the cursor and row objects.
buff_ds =  None
ds = None
print 'buffer complete'
print 'elapsed time: ',round(clock()-start,2),' seconds'
