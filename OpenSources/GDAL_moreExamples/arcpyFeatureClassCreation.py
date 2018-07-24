'''*********************************************
author: Galen Maclaurin
Date: 12/11/2012
Purpose: Create line feature with arcpy
*********************************************'''

import time
start = time.clock()
import arcpy
from arcpy import env
start2 =time.clock()
env.workspace = r'D:\data'
env.overwriteOutput = 1

theme = 'hikingRoute.shp'
coords = '/coords.txt'

with open(env.workspace+coords,'r') as outFile:
    xs,ys = (l.split(',') for l in outFile.readlines())

#The point object will be used to select each coordinate point before adding it to the array.
point = arcpy.Point()
array = arcpy.Array()

for coord in range(len(xs)):
    point.X = xs[coord]
    point.Y = ys[coord]
    array.add(point)

polyline = arcpy.Polyline(array)
arcpy.CopyFeatures_management(polyline,theme)

print 'elapsed time (total): ',round(time.clock()-start,2),' seconds'
print 'elapsed time (after arcpy import): ',round(time.clock()-start2,2),' seconds'
