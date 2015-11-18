import arcpy

arcpy.env.workspace = "U:/Shared/GIS/StuData/jtmccl390/FALL_2015/Python/Data/Exercise05/Results"
outputClass = "U:/Shared/GIS/StuData/jtmccl1390/FALL_2015/Python/Data/Exercise05/Results/parks_diss.shp"
arcpy.Dissolve_management("parks.shp", outputClass, "PARK_TYPE", "", "SINGLE_PART", "")
