import pprint
import numpy as np
import os

FILE_PATH = './KEN_ALL.CSV'

with open(FILE_PATH, encoding = 'Shift-JIS') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(',') for line in lines]

town_code_list = set(np.array(lines)[:,0])
town_num_list = []
first_col = [line[0] for line in lines]
l = len(town_code_list)
i = 1
for town_code in town_code_list:
    print(str(i)+"/"+str(l))
    i+=1
    town_num_list.append([str(first_col.count(town_code)).zfill(4), town_code])

os.system("cls")

rank_ten = sorted((town_num_list), reverse=True, key=lambda x:x[0])[:10]
rank_ten.insert(0, ["Rank  N. ", "Val ", "Code ", "Ken     ", "City"])
town_code_list = list(town_code_list)

lines_first_col = [line[0] for line in lines]
for i in range(1, 11):
    row = lines_first_col.index(rank_ten[i][1])
    rank_ten[i].append(lines[row][6])
    rank_ten[i].append(lines[row][7])
    rank_ten[i].insert(0, "Rank "+ str(i).zfill(2) +". ")

pprint.pprint(rank_ten)
print("")