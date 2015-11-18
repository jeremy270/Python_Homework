import arcpy
from arcpy import env

def available(result):
    if result == 'Available':
        return True
    else:
        return False


env.workspace = "U:/Shared/GIS/StuData/jtmccl390/FALL_2015/Python/Data/Exercise05/Results"

to_check = ['spatial', 'network', '3d', 'fake']
not_available = []

print("The following extensions are available: ")
for extension in to_check:
    if available(arcpy.CheckExtension(extension)):
        print("{} is available".format(extension))
    else:
        not_available.append(extension)
print("\nThe following extensions are not available: ")
for extension in not_available:
    print("{} is not available".format(extension))
