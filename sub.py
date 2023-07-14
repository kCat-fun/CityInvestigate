import os
import unicodedata

c = []

FILE_PATH = './KEN_ALL.CSV'

with open(FILE_PATH, encoding = 'Shift-JIS') as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
lines = [line.split(',') for line in lines]

katakana = [chr(i) for i in range(12449, 12532)]
remove_list = ['ァ','ィ','ゥ','ェ','ォ','ッ','ャ','ュ','ョ','ヮ','ヵ','ヶ']
for rl in remove_list:
    try:
        katakana.remove(str(rl))
    except:
        print("skip "+rl)

print(katakana)
print("len: "+str(len(katakana)))

count = [0]*len(katakana)
l=len(lines)
c = 1

for line in lines:
    # print(str(c)+"/"+str(l))
    c+=1
    i = 0
    for k in katakana:
        if(ord(unicodedata.normalize('NFKC', line[4])[1]) == ord(k)):
            count[i]+=1
        i+=1
            
os.system("cls")
            
for i in range(len(katakana)):
    print(katakana[i] + ": " + str(count[i]))