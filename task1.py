persons = input().split(', ')
out = ''
for person in range(len(persons)-2):
    out += 'от ' + persons[person] + ' ушёл, '
out += 'и от ' + persons[-2] + ' ушёл, а лиса — ам его! и нету колобка...'
print(out)