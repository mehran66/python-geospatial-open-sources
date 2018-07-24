import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from geopandas import GeoSeries, GeoDataFrame
from shapely.geometry import Polygon



# Set the current workspace
direc = r"C:\Users\David\Google Drive\OpenSources\data"
os.chdir(direc)

# Data Frames
swim = pd.read_csv("http://www.mosaic-web.org/go/datasets/swim100m.csv")
swim.head()
swim.columns
swim.describe()
swim.shape

swim.year.mean()
swim["year"].mean()
np.mean(swim["year"])
swim.groupby('sex')['year'].mean()

swim['minutes'] = swim.time/60. # Adding a New Variable
swim.insert(1, 'mins', swim.time/60.) # insert at a particular location in the columns
swim['time'] = swim.time/60. # redeﬁne an existing variable
swim.head()

#*************************************************************
# Create three simple polygons
p1 = Polygon([(0, 0), (1, 0), (1, 1)])
p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])

s = GeoSeries([p1, p2, p3])
s
print(s.area)


f, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5), sharey=True)
s.plot(axes=ax1)
ax1.set_title("Original Polygons")
ax1.set_xlim(-0.5, 3.5)
s.buffer(0.4).plot(axes=ax2)
ax2.set_title("Buffered Polygons")
ax2.set_ylim(-0.5, 1.5)
plt.show()

#*************************************************************
# Create from file (one line)
boros = GeoDataFrame.from_file(direc+r'\nybb\nybb.shp')
print(boros.area.sum())
boros.geometry
boros.geometry[0]

boros.set_index('BoroCode', inplace=True)


fig = plt.figure(figsize=(8, 8))
ax = boros.plot()  # Regular plot
# We can access and plot the geometries directly as well
ax = boros.geometry.convex_hull.plot(axes=ax)
plt.show()

population = pd.Series({'Manhattan': 1585873, 'Bronx': 1385108, 'Brooklyn': 2504700,
                     'Queens': 2230722, 'Staten Island': 468730})
population
boros = boros.set_index('BoroName')
boros['population'] = population
boros


plt.figure(figsize=(8, 8))
eroded = boros.geometry.buffer(-5280)
boros.plot(alpha=0.0)
eroded.plot()

#*************************************************************
import geopandas as gpd
df_geo = gpd.read_file(direc+r'\wifi\wifi.shp')
df_geo.head()

# Convert from NY State Plane to WGS84 (long/lat)
df_wgs84 = df_geo.to_crs(epsg=4326) # 4326 is the EPSG code for WGS84
print(df_geo.crs)
print(df_wgs84.crs)

ax = df_wgs84.plot() # This is all that's needed, but...
# ...here's a hack to plot things a bit more nicely (GeoPandas is still new!)
free = df_wgs84["type"] == "Free"  # Is it free?
col = {True: "green", False: "blue"}  # If free, green, otherwise blue
for i, l in enumerate(ax.lines):
    l.set_markersize(6)
    l.set_color(col[free[i]])
ax.axis('off')  # Turn off axes
plt.show()



