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
env.workspace = r'F:\GDAL\data'
env.overwriteOutput = 1

theme = 'areapoints.shp'
arcpy.Buffer_analysis(theme,'arcBuff.shp',500)

print 'elapsed time (total): ',round(time.clock()-start,2),' seconds'
print 'elapsed time (after arcpy import): ',round(time.clock()-start2,2),' seconds'