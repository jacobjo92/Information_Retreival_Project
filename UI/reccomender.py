import pandas as pd
import csv

def create_csv(title, description, size_of_retrieved_data):
    
    
    fields = ['Title', 'Description']
    rows = []
    
    for i in range(0,size_of_retrieved_data):
        rows.append([title[i], description[i]])
        
    print(rows)
    with open('metadata.csv','w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
             

metadata = pd.read_csv('metadata.csv',low_memory=False)

metadata.head(3)



