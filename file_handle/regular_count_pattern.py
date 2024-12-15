import re
pattern = "Siddhartha"

def count_string(pattern):
    count = 0
    for line in open("siddhartha.txt", encoding="utf-8"):
        result = re.search(pattern, line)
        if result != None:
            count += 1
    return count
        
result = count_string(pattern)
print(result)

