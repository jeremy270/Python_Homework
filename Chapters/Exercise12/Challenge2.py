##import parcelclass
##myparcel = parcelclass.Parcel("SFR", 125000)
##print "Land use: ", myparcel.landuse
##mytax = myparcel.assessment()
##print "Tax assessment: ", mytax



import arcpy
import parcelclass
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise12"
fc = "parcels.shp"
cursor = arcpy.da.SearchCursor(fc, ["FID", "Landuse", "Value"])
for row in cursor:
    myparcel = parcelclass.Parcel(row[1], row[2])
    mytax = myparcel.assessment()
print "{0}: {1}".format(row[0], mytax)
