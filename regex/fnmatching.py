import os
from fnmatch import fnmatch

path =  "C:\\Users\\uttam\\Downloads"
path = os.chdir(path)
lst = os.listdir(path)

for file in lst:
    if fnmatch(file, "*python*.pdf"):
    # if fnmatch(file, "*[.pdf|.csv]"):
        print(file)


pdf_files = [file for file in lst if fnmatch(file, "*.pdf")]

print(pdf_files)






















