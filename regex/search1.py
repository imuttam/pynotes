import re
file = open('romeo.txt', encoding='utf-8')

for line in file:
    line = line.strip()
    # if re.search('Romeo', line):
    # if re.search('.omeo', line):# in dot means any thing
    if re.search('^Romeo', line):# start with Romeo
        print(line)