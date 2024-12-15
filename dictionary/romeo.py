fname = 'romeo.txt'

try:
    fhand = open(fname, encoding='utf-8')
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

# print(counts)
# word with maximum frequency 

lst = []
for k,v in counts.items():
    lst.append((v,k))

sort_lst = sorted(lst, reverse=True)
print(sort_lst)