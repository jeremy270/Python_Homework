import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise08"
fc = "Hawaii.shp"
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
xlist = []
ylist = []
for row in cursor:
  for part in row[1]:
    for point in part:
      xlist.append(point.X)
      ylist.append(point.Y)
xlist.sort()
ylist.sort()
max_x = xlist[-1]
min_x = xlist[0]
max_y = ylist[-1]
min_y = ylist[0]

coordlist = [(min_x,min_y),(max_x,min_y),(max_x,max_y),(min_x,max_y),(min_x,min_y)]
             
arcpy.CreateFeatureclass_management("U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise08", "Results/envelope1.shp", "Polygon")
cursor = arcpy.da.InsertCursor("Results/envelope1.shp", ["SHAPE@"])
array = arcpy.Array()
ident = 0
for coord in coordlist:
   ID, X, Y = ident, coord[0],coord[1]
   array.add(arcpy.Point(X, Y))
   ident += 1
cursor.insertRow([arcpy.Polygon(array)])
del cursor
