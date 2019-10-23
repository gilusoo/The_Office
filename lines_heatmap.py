# Dataset Available at: https://docs.google.com/spreadsheets/d/18wS5AAwOh8QO95RwHLS95POmSNKA2jjzdt0phrxeAE0/edit#gid=747974534

'''The purpose of this analysis is to look at every spoken line from the NBC hit television show 'The Office' and create
    a heat map of each character to lines spoken. The final results included in the figure were filtered to make it more
    interesting.'''

import re
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
import seaborn as sns

datafile = 'theOffice.csv'

char_to_idx = {'Michael':0, 'Dwight':1, 'Jim':2, 'Pam':3, 'Andy':4, 'Kevin':5, 'Angela':6}
curr_counts = [0,0,0,0,0,0,0]
line_hits = {}

with open(datafile, 'r') as data:
    next(data)
    for row in data:
        row = row.strip().split(',')
        # print(row)
        if len(row) == 7:
            char = row[5]
            line = re.sub("[^a-zA-Z]+", " ", row[4])
            line = line.lower().strip()
            line_hits[line] = line_hits.get(line, [0,0,0,0,0,0,0])
            if char in char_to_idx.keys():
                line_hits[line][char_to_idx[char]] += 1

figure = []
new_line_hits = {}
for k, v in line_hits.items():
    if len(k) < 10:
        continue
    if k.startswith(' '):
        continue
    if sum(v) > 5 and sum(v) < 30:
        new_line_hits[k] = v
        figure.append(v)

list_of_lines = sorted(new_line_hits.items(), key= lambda x:x[1], reverse=True)
used_lines = []
for line in list_of_lines[0:30]:
    used_lines.append(line[0])
    print(line[0])

ax = plt.axes()
ax.set_title('The Office Spoken Lines')
sns.set(font_scale=0.75)
ax = sns.heatmap(data=sorted(figure[0:30], reverse=True), xticklabels=char_to_idx.keys(), yticklabels=used_lines)
plt.yticks(rotation=0)
plt.show(block=True)