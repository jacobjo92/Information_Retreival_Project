import requests
import json
from snakemd import Document
COLLECTION_NAME_1 = "getyourguide"
COLLECTION_NAME_2 = "swisstour"
COLLECTION_NAME_3 = "viator"
RESULT_OUTPUT_PATH ="result"


def create_md(doc_name, title,description, price,rating):
    resultDoc = Document(doc_name)
    resultDoc.add_header(title)
    resultDoc.add_paragraph(description)
    resultDoc.add_paragraph(price)
    resultDoc.add_paragraph(rating)
    
    return resultDoc
    
    

def cleanup_string(input):
    input = input.replace("\n", "")
    return input

# UI for querying the localhost.
def query(choice = 1, user_query = "."):
    URL_1 = "http://localhost:8983/solr/" + COLLECTION_NAME_1 + "/select?df=title&indent=true&q.op=OR&q="+user_query
    URL_2 = "http://localhost:8983/solr/" + COLLECTION_NAME_2 + "/select?df=title&indent=true&q.op=OR&q="+user_query
    URL_3 = "http://localhost:8983/solr/" + COLLECTION_NAME_3 + "/select?df=title&indent=true&q.op=OR&q="+user_query
    if (choice == 1):
        URL = URL_1
    elif (choice == 2):
        URL = URL_2
    elif (choice == 3):
        URL = URL_3
    res = requests.get(URL)
    
    
    # Testing snakemd

    
    if res.json()['response']['numFound'] > 0:
        print("Number of results: " + str(res.json()['response']['numFound']))
        for a in res.json()['response']['docs']:
            
            title = cleanup_string(str(a['title'][0]))
            description = "Description: " + cleanup_string(str(a['Description_'][0]))
            price = "Price: " + cleanup_string(str(a['price'][0]))
            rating = "Rating: " + cleanup_string(str(a['rating'][0]))
            document = create_md("Results of your query",title,description,price,rating)
            document.output_page(RESULT_OUTPUT_PATH)
            print(document)
            
            
    else:
        print("No documents were found for your query.")