persons = input().split(', ')
out = ''
if len(persons) < 3:
    raise TypeError('Too few characters! - Please, enter at least 3 characters')
if persons[-1] != 'лиса':
    raise ValueError("The last character must be 'лиса'!")
for person in range(len(persons)-2):
    out += 'от ' + persons[person] + ' ушёл, '
out += 'и от ' + persons[-2] + ' ушёл, а лиса — ам его! и нету колобка...'
print(out)