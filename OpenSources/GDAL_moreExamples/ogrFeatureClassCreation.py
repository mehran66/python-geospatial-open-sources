'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Purpose: Create line feature with OGR
Sources: adapted from code by Chris Garrard
http://www.gis.usu.edu/~chrisg/python/2009/
*********************************************'''

from time import clock
start = clock()
from osgeo import ogr
import os

path = r'D:\data'
os.chdir(path)
theme = 'hikingRoute.shp'
coords = '/coords.txt'

with open(path+coords,'r') as outFile:
    xs,ys = (l.split(',') for l in outFile.readlines())

#create a driver object to read shapefiles
dvr = ogr.GetDriverByName('ESRI Shapefile')
#delete shapefiles with the same name
if os.path.exists(theme):
    dvr.DeleteDataSource(theme)

#create a datasource object with the driver
ds = dvr.CreateDataSource(theme)
#create a layer object with the datasource object
lyr = ds.CreateLayer(theme[:-4],geom_type=ogr.wkbLineString)

#create a feature
featureDefn = lyr.GetLayerDefn()
feature = ogr.Feature(featureDefn)

#finally create the line from points
line = ogr.Geometry(ogr.wkbLineString)
for p in range(len(xs)):
    line.AddPoint(float(xs[p]),float(ys[p]))

#set the line as the feature geometry
feature.SetGeometry(line)

#save the feature to the layer object
lyr.CreateFeature(feature)
#clean up
ds = None

print 'elapsed time: ',round(clock()-start,2),' seconds'