with open('../words.txt') as file:
    print(dir(file))
    headers = next(file).strip()
    print(headers)
    line1 = file.__next__().strip("\n")
    print(line1)
    line2 = file.readline().strip()
    print(line2)