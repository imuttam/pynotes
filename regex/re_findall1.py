# Search for lines that have an at sign between characters
import re
mails = set()
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    # x = re.findall('\S+@\S+', line)
    # pattern = r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]'
    pattern = r'[a-zA-Z0-9]\S+@\S+[a-zA-Z]' # more strict , start and end with char like a-z,A-Z,0-9
    # pattern_x = r'^X\S*' # pattern that start with X with non whitespace
    pattern_x = r'^X\S*: \S*'
    
    x = re.findall(pattern_x, line)
    if len(x) > 0:
        print(*x)
        mails.add(*x)
# print(mails)