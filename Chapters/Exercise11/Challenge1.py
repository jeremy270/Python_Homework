"""  Original Code

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
FC = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if fields.name == "NAME"
        for row in rows:
        print "Name = {0}".format(row.getValue(field.name))
"""


import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise11"
fc = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if field.name == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))


"""
    
    Line 4: it should be lower case fc.
    Line 8: missing a colon on the if statemente.
    Line 8: "fields.name" has an "s"
    Line 10: the print statement was not indented

"""    
