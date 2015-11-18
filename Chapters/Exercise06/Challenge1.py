import arcpy
from arcpy import env
env.workspace = "C:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc).shapeType
   print("{0} is {1} feature class".format(fc, fcdescribe))
