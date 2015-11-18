import os.path
import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise06"

if not os.path.isdir(env.workspace + "/Results/mydb.gdb"):
    print ("Creating File GDB")
    arcpy.CreateFileGDB_management("U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise06/Results", "NM.gdb")


env.workspace ="U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise06"Results/NM.gdb"
print("Copying Features")
for feature in arcpy.ListFeatureClasses():
    dataset = arcpy.Describe(feature)
    if dataset.shapeType == "Polygon":
        arcpy.CopyFeatures_management(feature, "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise06/Results/mydb.gdb/" + dataset.name)
