import pandas as pd
import csv


def create_csv(title, description, rating, size_of_retrieved_data):

    fields = ['Title', 'Description', 'Rating']
    rows = []

    for i in range(0, size_of_retrieved_data):
        rows.append([title[i], description[i], rating[i]])

    with open('metadata.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    ratings = pd.read_csv('metadata.csv', sep='\t', names=fields)

    metadata = pd.read_csv('metadata.csv', low_memory=False)

    movies_merge = pd.merge(ratings, metadata, on='Rating')
    print(movies_merge.head())
