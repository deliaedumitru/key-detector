import sys
import os

MIDICSV_PATH = ".\Midicsv.exe"

# run as
# python midi-to-csv.py midi_folder dest_folder

directory = os.fsencode(sys.argv[1])
for f in os.listdir(directory):
    fileName = os.fsdecode(f)
    splitName = fileName.split('.')
    if len(splitName) == 2 and splitName[1] == "mid":
        command = MIDICSV_PATH + " \"" + sys.argv[1] + "\\" + fileName + "\" \"" + sys.argv[2] + "\\" + splitName[0] + ".csv\""
        os.system(command)
