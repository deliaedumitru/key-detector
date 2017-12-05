import sys
import os

# run as
# python csv-to-ascii.py csv-dir

directory = os.fsencode(sys.argv[1])

for f in os.listdir(directory):
    fileName = os.fsdecode(f)
    splitName = fileName.split('.')
    if len(splitName) == 2 and splitName[1] == "csv":
        os.system("python translate.py \"" + sys.argv[1] + "\\" + fileName + "\"")