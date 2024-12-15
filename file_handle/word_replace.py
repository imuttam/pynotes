writer = open("replaced.txt", "w")

with open("siddhartha.txt", encoding="utf-8") as file:
    for line in file:
        line = line.replace("Siddhartha", "Gautam")
        writer.write(line)



    
