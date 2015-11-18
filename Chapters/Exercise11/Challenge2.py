""" Original Code from Challenge 2

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data\Exercise09"
raster = "landcover.tiff"
desc = arcpy.describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."

"""

import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise11"
raster = "landcover.tiff"
desc = arcpy.describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."


"""

    Line 3: forward slashes instead of back slashes
    Line 4: .tiff does not exist (.tif)
    Line 5: .Describe should be capitalized
    Line 6: Mean in desc.MeanCellHeight statement should be lowercase
    Line 7: Mean in desc.MeanCellWidth statement should be lowercase
    Line 8: desc.spatialReference should be capitalized to Spatial.

"""
