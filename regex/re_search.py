import re 

file = open('mbox-short.txt')
for line in file:
    line = line.strip()
    # if re.search('^From:', line):
    if re.search('^From:.*', line):
        print(line)
print('****************************')

