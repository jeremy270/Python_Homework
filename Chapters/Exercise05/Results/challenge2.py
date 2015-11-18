import arcpy
from arcpy import env

env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015//Python/Data/Exercise05/Results"
arcpy.AddXY_management("hospitals.shp")
