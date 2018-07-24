'''*********************************************
author: Galen Maclaurin
Date: 2/24/2014
Purpose: Get feature info with OGR
*********************************************'''

from osgeo import ogr
path = r'F:\GDAL\data'
sName = path+'/watersheds_3D.shp'

#open shapefile
ds = ogr.Open(sName)
#get layer object
lyr = ds.GetLayer()
#get feature object, index the row you want
feat = lyr[0]
#get geometry object
geom = feat.GetGeometryRef()
#get array, this is like getPart(), 0 for single part feature classes
array = geom.GetGeometryRef(0)
#get points, indexed
array.GetPoint(0)