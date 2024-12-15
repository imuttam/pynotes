records = []

students = {}

with open('./score.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        records.append((row[1],row[3]))

print(records)


with open('./score.csv', 'rt') as f:
    next(f) # Skip header
    for line in f:
        row = line.split(',')
        students[row[1]] = row[3]

print(students)