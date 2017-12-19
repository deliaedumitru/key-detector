import pandas as pd
import numpy as np

DATA = 'data_keys.csv'
CLASS = 'key'

MINOR_KEYS = ['G sharp minor', 'A minor', 'B flat minor', 'B minor', 'C minor', 'C sharp minor', 'D minor', 'D sharp minor', 'E minor', 'F minor', 'F sharp minor', 'G minor']
MAJOR_KEYS = ['A flat major', 'A major', 'B flat major', 'B major', 'C major', 'C sharp major', 'D major', 'E flat major', 'E major', 'F major', 'F sharp major', 'G major']

set = pd.read_csv(DATA)
set_matrix = set.as_matrix()
features = set_matrix[:, :-1]
classes = set_matrix[:, -1]
classes = np.reshape(classes, (classes.shape[0], 1))

new_set = set_matrix

for i in range(1, 12):
    features = np.roll(features, 1, axis=1)
    for cls in classes:
        if cls[0].split(' ')[-1] == 'minor':
            cls[0] = MINOR_KEYS[(MINOR_KEYS.index(cls[0]) + 1) % len(MINOR_KEYS)]
        elif cls[0].split(' ')[-1] == 'major':
            cls[0] = MAJOR_KEYS[(MAJOR_KEYS.index(cls[0]) + 1) % len(MAJOR_KEYS)]
    shifted_set = np.append(features, classes, 1)
    new_set = np.append(new_set, shifted_set, 0)

df = pd.DataFrame(new_set, columns=['C', 'C sharp', 'D', 'D sharp', 'E', 'F', 'F sharp', 'G', 'G sharp', 'A', 'A sharp', 'B', 'key'])
df.to_csv("new_data.csv", index = False)