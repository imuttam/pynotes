with open("siddhartha.txt", encoding="utf-8") as file:
    for line in file:
        for word in line.strip().split():
            if word.lower() == "siddhartha":
                print(line)


