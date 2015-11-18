import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise08"
env.overwriteOutput = True
outpath = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise08/results"
newfc = "Results/square.shp"

arcpy.CreateFeatureclass_management(outpath, newfc, "Polygon")

infile = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise08/results/square.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line, " ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polygon(array)])
fileinput.close()
del cursor
