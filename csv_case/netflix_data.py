# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:43:50 2024

@author: uttam
"""

""" understanding handling csv file using csv """

import csv

movie_list = []

file = open('../data_set/netflix_titles.csv',encoding='utf-8')

headers = next(file)
headers = headers.split(',')
print(headers)
rows = csv.reader(file)

for row in rows:
    
    d = dict(zip(headers, row))
    movie_list.append(d)
    
#print(movie_list)
print("MOVIE NAME: YEAR")
for movie in movie_list:
    if movie['country'] == 'India':
        print(f"movie['title']:movie['release_year']")

