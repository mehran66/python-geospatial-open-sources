'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Updated: 03/14/2016 , Stefan Leyk
Purpose: Simple Buffer example using OGR
*********************************************'''

from time import clock
start = clock()
import os
from osgeo import ogr

# Define variables you need
path = r'C:\GIS3\data\cl08data'
#change the working directory
os.chdir(path)
theme = 'areapoints.shp'
buffTheme = 'buffOutput.shp'
buffDist = 500

# Open the feature class, creating an 'ogr' object
ds = ogr.Open(theme)
# Get the driver from the ogr object. The driver object is an interface to work
# with a specific vector data format (i.e. ESRI shapefile in this case).
dvr = ds.GetDriver()
# Check to see if the output file exists and delete it if so.
if os.path.exists(buffTheme):
    dvr.DeleteDataSource(buffTheme)
    print buffTheme, "existed and has been deleted"

# Get the layer object from the ogr object. This is kind of like a cursor object.
lyr = ds.GetLayer()
# Get the number of features. the layer object is an iterable object.
numFeat = len(lyr)

# Create an empty feature class to populate with buffer features. This is stored
# in memory as an emtpy ogr object.
buff_ds = dvr.CreateDataSource(buffTheme)
# Create a layer object from the empty ogr object.
outLyr = buff_ds.CreateLayer(buffTheme[:-4],lyr.GetSpatialRef(),ogr.wkbPolygon)

# Adding a field takes two steps: create a field definition and then use that
# to create the field
# Create a field definition
fd = ogr.FieldDefn('myField',ogr.OFTString)
# Create field with the field definition
outLyr.CreateField(fd)
# Similarly, you need to use a layer definition to create a feature
lyrDef = outLyr.GetLayerDefn()
# Iterate through the features in the layer object (like with a cursor)
for feat in lyr:
    #get the geometry object from the feature object.
    geom = feat.GetGeometryRef()
    #create a new feature using the layer definition create outside the loop
    outFeat = ogr.Feature(lyrDef)
    #set the feature's geometry as the buffered geometry
    outFeat.SetGeometry(geom.Buffer(buffDist))
    #set field value for feature
    outFeat.SetField('myField','someText'+str(feat.GetFID()))
    #save the new feature in the output layer created outside the loop
    outLyr.CreateFeature(outFeat)

# Clean up, remove reference to the datasource objects, this is like deleting
# the cursor and row objects.
buff_ds =  None
ds = None
print 'Buffer vector features complete'
print 'Elapsed time: ',round(clock()-start,2),' seconds'
