#https://github.com/jswhit/pyproj
#http://spatialreference.org/ref/epsg/
# Converting coordinates with PyProj
import pyproj
from pyproj import Proj

# projection 1: UTM zone 15, grs80 ellipse, NAD83 datum
# (defined by epsg code 26915)
p1 = Proj(init='epsg:26915')
# projection 2: UTM zone 15, clrk66 ellipse, NAD27 datum
p2 = Proj(init='epsg:26715')
# find x,y of Jefferson City, MO.
x1, y1 = p1(-92.199881,38.56694)
# transform this point to projection 2 coordinates.
x2, y2 = pyproj.transform(p1,p2,x1,y1)

# process 3 points at a time in a tuple
lats = (38.83,39.32,38.75) # Columbia, KC and StL Missouri
lons = (-92.22,-94.72,-90.37)
x1, y1 = p1(lons,lats)
x2, y2 = pyproj.transform(p1,p2,x1,y1)

#Proj4 Format
myProj = Proj("+proj=utm +zone=2K, +south +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
x2, y2 = pyproj.transform(p1,myProj,x1,y1)