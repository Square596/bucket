import json
import os
import csv
import shutil


home_path = os.path.expanduser("~")
working_dir = os.path.join(home_path, 'hw3')

# hw3:
os.makedirs(working_dir, exist_ok=True)

# hw3/file.txt
with open(os.path.join(working_dir, 'file.txt'), 'w') as text_file:
    text_file.write('\n'.join(['Do you believe in Heaven above?', 'Do you believe in love?', "Don't tell a lie, don't be false or untrue", 'It all comes back to you']))

# hw3/file.json
with open(os.path.join(working_dir, 'file.json'), 'w') as json_file:
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
    }, json_file)

# hw3/file.csv
csv_example = ['Cancer Type,D-Loop,mRNAs,tRNAs,rRNAs,Nucleotide Position of Deletions,Increase of mtDNA copy \#,Decrease of mtDNA copy #'.split(','),
               'Bladder,1,1,0,1,15642-15662,0,0'.split(','),
               'Breast,1,1,1,1,8470-13447 and 8482-13459,0,1'.split(','),
               'Oral,1,1,0,0,8470-13447 and 8482-13459,0,0'.split(',')]

with open(os.path.join(working_dir, 'file.csv'), 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(csv_example[0])
    for i in range(1, len(csv_example)):
        writer.writerow(csv_example[i])

# hw3/folder/
os.makedirs(os.path.join(working_dir, 'folder'), exist_ok=True)

# content of hw3/
files = []
for object in os.listdir(working_dir):
    if os.path.isfile(os.path.join(working_dir, object)):
        files.append([object, os.path.getctime(os.path.join(working_dir, object))])

sorted_files = []
for file_name in sorted(files, key=lambda x: x[1]):
    sorted_files.append(file_name[0])
print(*sorted_files)

# removing hw3
shutil.rmtree(working_dir)