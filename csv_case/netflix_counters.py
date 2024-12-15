import csv
from collections import Counter

# Initialize a Counter to keep track of the number of titles by country
total_movies = Counter()
release_year = Counter()

with open('./data_set/netflix_titles.csv', encoding='utf-8') as file:
    rows = csv.reader(file)
    headers = next(rows)  # Get headers from rows instead of file for accuracy
    # print(headers)  # Check headers

    for row in rows:
        # Increment the count for each country in the Counter
        country = row[5]
        year = row[7]
        if country:  # Check if the country field is not empty
            total_movies[country] += 1
        if year:
            release_year[year] +=1
     

# Print the total movies count by country
# print(total_movies)
print(release_year)

movies_count = {}
def year_wise_movies_count():
    with open('./data_set/netflix_titles.csv', encoding='utf-8') as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            year = row[7]
            if year not in movies_count:
                movies_count[year] = 1
            else:
                movies_count[year] += 1
    return movies_count

print(year_wise_movies_count())


