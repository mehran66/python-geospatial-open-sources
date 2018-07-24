'''*********************************************
author: Galen Maclaurin
Date: 3/16/2014
Purpose: Buffer example
*********************************************'''

from time import clock
start = clock()
import os
from osgeo import ogr

def bufferFC(iName,oName,bDist):
    ds = ogr.Open(iName)
    dvr = ds.GetDriver()
    lyr = ds.GetLayer()
    if os.path.exists(buffTheme):
        dvr.DeleteDataSource(buffTheme)
    buff_ds = dvr.CreateDataSource(oName)
    outLyr = buff_ds.CreateLayer(oName[:-4],lyr.GetSpatialRef(),ogr.wkbPolygon)
    lyrDef = outLyr.GetLayerDefn()
    for feat in lyr:
        geom = feat.GetGeometryRef()
        outFeat = ogr.Feature(lyrDef)
        outFeat.SetGeometry(geom.Buffer(bDist))
        outLyr.CreateFeature(outFeat)
    buff_ds =  None
    ds = None
    return

path = r'C:\GEOG4303\GDAL\data'
#change the working directory
os.chdir(path)
theme = 'areapoints.shp'
buffTheme = 'buffOutput.shp'
buffDist = 500

bufferFC(theme,buffTheme,buffDist)

print 'buffer complete'
print 'elapsed time: ',round(clock()-start,2),' seconds'
