# run as
# py csv_to_note_weights.py csv-file dest-file

import sys

csv = open(sys.argv[1], "r")
content = []

# clean unnecessary lines
for line in csv:
    if "Note_on_c" in line:
        fields = line.split(", ")
        content.append(fields)

note_freq = [0] * 12

# find each note start 
for i in range(0, len(content)):
    if content[i][2] == "Note_on_c" and int(content[i][5]) != 0:
        note_freq[int(content[i][4]) % 12] += 1


note_freq = [el / sum(note_freq) for el in note_freq]

data_file = open(sys.argv[2], "w")
data_file.write('\n'.join([str(el) for el in note_freq]))