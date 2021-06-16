import glob
import re

path = r"D:\maya\scene_file_V01.ma"
# If there are many files then u can use the wild card * on path eg. path = r"D:\maya\*.ma"

# this code will iterate through all the files for finding "Mentel Ray plugin" requirement. If it finds it will output the path to the file.
for obj in glob.glob(path):
    files = open(obj, "r")
    for line in lines.readlines():
        if re.search("Mayatomr", line, re.I):
            print(obj)
