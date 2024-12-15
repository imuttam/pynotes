import csv

def medals_tup():
    gold_medals = {}
    with open("data_set/athlete_events.csv","r") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            medal = row[-1]
            country = row[6]
            if medal == "Gold":
                if country not in gold_medals:
                    gold_medals[country] = 1
                else:
                    gold_medals[country] += 1

        
    return gold_medals

medals = medals_tup()

medals_sort = sorted(list(zip(medals.values(),medals.keys())), reverse=True)
# Swapping the tuples using lambda
swapped_medals_sort = list(map(lambda x: (x[1], x[0]), medals_sort))




items = list(medals.items())
medals_sorted = sorted(items, key=lambda i: i[1], reverse=True)
print(medals_sort[:10])

print(swapped_medals_sort[:10])

