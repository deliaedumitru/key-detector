import sys
from operator import itemgetter
csv = open(sys.argv[1], "r")
name = sys.argv[2]
txt = open(name, "w")

# run as
# python translate.py csv-file dest-file

OFFSET = 33

content = []

# clean unnecessary lines
for line in csv:
    if "Note_on_c" in line or "Note_off_c" in line:
        fields = line.split(", ")
        content.append(fields)

notes = []

# find start time & end time for each note    
for i in range(0, len(content)):
    if content[i][2] == "Note_on_c" and content[i][5] != '0':
        for j in range(i, len(content)):
            if (content[j][2] == "Note_off_c" or (content[j][2] == "Note_on_c" and int(content[j][5]) == 0)) and content[j][4] == content[i][4]:
                notes.append((content[i][4], content[i][1], content[j][1]))
                break

words = {}

# find notes that are being played simultaneously
for i in range(0, len(notes)):
    word = chr(int(notes[i][0]) + OFFSET)
    if notes[i][1] in words:
        words[notes[i][1]] += word
    else:
        words[notes[i][1]] = word

sorted_words = sorted(words.items(), key = lambda x: int(x[0]))

phrase = ""
for tup in sorted_words:
    phrase += tup[1] + " "

txt.write(phrase)
