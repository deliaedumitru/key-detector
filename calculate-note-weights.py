import sys
from collections import Counter
from operator import itemgetter
import pandas

# run as
# py translate.py csv-file dataset-file

csv = open(sys.argv[1], "r")

KEYS_CSV_PATH = "keys.csv"
DATA_FILE_PATH = "data_keys.csv"

def getKey(filename):
    keys = pandas.read_csv(KEYS_CSV_PATH, dtype={'bwv': object})
    bwv_str = filename.split('\\')[-1][:4]
    return keys.loc[keys['bwv'] == bwv_str]['key'].iloc[0]

content = []

# clean unnecessary lines
for line in csv:
    if "Note_on_c" in line:
        fields = line.split(", ")
        content.append(fields)

note_freq = [0] * 12

# count each note class    
for i in range(0, len(content)):
    if content[i][2] == "Note_on_c" and int(content[i][5]) != 0:
        note_freq[int(content[i][4]) % 12] += 1

# compute the frequency of each note class
note_freq = [el / sum(note_freq) for el in note_freq]

key = getKey(sys.argv[1])

data_file = open(DATA_FILE_PATH, "a")
data_file.write(','.join([str(el) for el in note_freq]) + "," + key + "\n")