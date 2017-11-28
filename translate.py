import sys
from collections import Counter
from operator import itemgetter
import pandas

csv = open(sys.argv[1], "r")
# name = sys.argv[2]
# txt = open(name, "w")

# run as
# python translate.py csv-file dest-file

KEYS_CSV_PATH = "keys.csv"

DATA_FILE_PATH = "data.csv"

def getKey(filename):
    keys = pandas.read_csv(KEYS_CSV_PATH, dtype={'bwv': object})
    bwv_str = filename.split('\\')[-1][:4]
    return keys.loc[keys['bwv'] == bwv_str]['key'].iloc[0]
    
def getKeyType(filename):
    keys = pandas.read_csv(KEYS_CSV_PATH, dtype={'bwv': object})
    bwv_str = filename.split('\\')[-1][:4]
    return keys.loc[keys['bwv'] == bwv_str]['key'].iloc[0].split()[-1]

content = []

# clean unnecessary lines
for line in csv:
    if "Note_on_c" in line:
        fields = line.split(", ")
        content.append(fields)

notes = []

# find start time & end time for each note    
for i in range(0, len(content)):
    if content[i][2] == "Note_on_c" and int(content[i][5]) != 0:
        notes.append(int(content[i][4]) % 12)

note_counter = Counter(notes)
freq_pseudo_dict = sorted(note_counter.items(), key = lambda x: x[0])
freq_list_abs = [el[1] for el in freq_pseudo_dict]

freqs = [el / sum(freq_list_abs) for el in freq_list_abs]

key_type = getKeyType(sys.argv[1])

data_file = open(DATA_FILE_PATH, "a")
data_file.write(','.join([str(el) for el in freqs]) + "," + key_type + "\n")