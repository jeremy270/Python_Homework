import arcpy
from arcpy import env

env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise10"

mxd = arcpy.mapping.MapDocument("U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd)
lyrlist = arcpy.mapping.ListLayers(mxd, "Parks")

dflist = arcpy.mapping.ListDataFrames(mxd)
for lyr in lyrlist:
    if lyr.name == "parks":
        if lyr in df != "parks":
            arcpy.mapping.AddLayer(df, lyr, "AUTO_ARRANGE" )
        


mxd.save()
del mxd
