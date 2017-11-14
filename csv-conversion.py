import sys
import os

MIDICSV_PATH = ".\Midicsv.exe"

# run as
# python csv-conversion.py midi-folder dest-folder

directory = os.fsencode(sys.argv[1])
for f in os.listdir(directory):
    fileName = os.fsdecode(f)
    splitName = fileName.split('.')
    if len(splitName) == 2 and splitName[1] == "mid":
        os.system(MIDICSV_PATH + " " + fileName + " " + sys.argv[2] + "\\" + splitName[0] + ".csv")



