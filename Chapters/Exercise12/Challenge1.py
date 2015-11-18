import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise12"
import mycount

print(mycount.countstringfields("streets.shp"))
