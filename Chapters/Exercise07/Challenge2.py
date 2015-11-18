import arcpy
from arcpy import env
env.workspace = "U:/Shared/GIS/StuData/jtmccl1390/Fall_2015/Python/Data/Exercise07"

fc = "roads.shp"
newfield = "FERRY"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)

cursor = arcpy.da.UpdateCursor(fc, ["FEATURE","FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1] = "NO"
    cursor.updateRow(row) 
