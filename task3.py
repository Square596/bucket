import json
import os
import csv
import shutil


home_path = os.getenv('USERPROFILE').replace('\\', '/')

# hw3:
try:
    os.mkdir(home_path+'/hw3')
except FileExistsError: pass

# hw3/file.txt
with open(home_path+'/hw3/file.txt', "w") as x:
    x.write("Do you believe in Heaven above?\nDo you believe in love?\nDon't tell a lie, don't be false or untrue\nIt all comes back to you")

# hw3/file.json
with open(home_path+'/hw3/file.json', 'w') as y:
    json.dump({
    "movies": [
        {
            "name": "Полночь в Париже",
            "release_year": 2011,
            "director": "Вуди Аллен"
        },
        {
            "name": "Гравити Фолз",
            "release_year": 2012,
            "creator": "Алекс Хирш"
        },
        {
            "name": "Окно во двор",
            "release_year": 1954,
            "director": "Альфред Хичкок"
        }
    ]
}, y)

# hw3/file.csv
csv_example = ['Cancer Type,D-Loop,mRNAs,tRNAs,rRNAs,Nucleotide Position of Deletions,Increase of mtDNA copy \#,Decrease of mtDNA copy #'.split(','),
               'Bladder,1,1,0,1,15642-15662,0,0'.split(','),
               'Breast,1,1,1,1,8470-13447 and 8482-13459,0,1'.split(','),
               'Oral,1,1,0,0,8470-13447 and 8482-13459,0,0'.split(',')]
with open(home_path+'/hw3/file.csv', 'w') as z:
    writer = csv.writer(z)
    writer.writerow(csv_example[0])
    for i in range(1,len(csv_example)):
        writer.writerow(csv_example[i])

# hw3/folder/
try:
    os.mkdir(home_path+'/hw3/folder')
except FileExistsError: pass

# content of hw3/
pre_pre_out = []
pre_out = []
out = []
for root, dirs, files in os.walk(home_path+'/hw3'):
    pre_pre_out.append(files)
for i in pre_pre_out[0]:
    pre_out.append([i, os.path.getctime(home_path+'/hw3/'+i)])
for i in sorted(pre_out, key=lambda x: x[1]):
    out.append(i[0])
print(*out)

# removing hw3
shutil.rmtree(home_path+'/hw3')