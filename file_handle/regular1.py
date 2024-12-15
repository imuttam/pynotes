import re
pattern = "Siddhartha"

def find_first(pattern):
    for line in open("siddhartha.txt", encoding="utf-8"):
        result = re.search(pattern, line)
        if result != None:
            return result
        
result = find_first(pattern)
pattern2 = "^Gutenberg"
result2 = find_first(pattern2)
pattern3 = "Gutenberg$"
print(result.string)
print(result2.string)
result3 = find_first(pattern3)
print(result3.string)