import arcpy
from arcpy import env

shortpath = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise09"
env.workspace = shortpath
rasterlist = arcpy.ListRasters()
arcpy.CreatePersonalGDB_management(shortpath + "/Results", "myrasters.gdb")

for raster in rasterlist:
    desc = arcpy.Describe(raster)
    rname = desc.baseName
    outraster = shortpath + "/Results/myrasters.gdb/" + rname
    arcpy.CopyRaster_management(raster, outraster)
