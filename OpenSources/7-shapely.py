from shapely.geometry import Point
patch = Point(0.0, 0.0).buffer(10.0)
patch.area
Point(0,0).distance(Point(1,1))

from shapely.geometry import LineString
line = LineString([(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)])
line.length
dilated = line.buffer(0.5)
eroded = dilated.buffer(-0.3)

from shapely.geometry import Polygon
polygon = Polygon([(0, 0), (1, 1), (1, 0)])
polygon.area
polygon.length


#Exploring the path of Hurican Katrina
from shapely.geometry import LineString
lons = [-75.1, -75.7, -76.2, -76.5, -76.9, -77.7, -78.4, -79.0,
        -79.6, -80.1, -80.3, -81.3, -82.0, -82.6, -83.3, -84.0,
        -84.7, -85.3, -85.9, -86.7, -87.7, -88.6, -89.2, -89.6,
        -89.6, -89.6, -89.6, -89.6, -89.1, -88.6, -88.0, -87.0,
        -85.3, -82.9]
lats = [23.1, 23.4, 23.8, 24.5, 25.4, 26.0, 26.1, 26.2, 26.2, 26.0,
        25.9, 25.4, 25.1, 24.9, 24.6, 24.4, 24.4, 24.5, 24.8, 25.2,
        25.7, 26.3, 27.2, 28.2, 29.3, 29.5, 30.2, 31.1, 32.6, 34.1,
        35.6, 37.0, 38.6, 40.1]

# Turn the lons and lats into a shapely LineString
katrina_track = LineString(zip(lons, lats))














