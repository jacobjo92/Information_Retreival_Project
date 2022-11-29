import requests
import json
COLLECTION_NAME_1 = "getyourguide"
COLLECTION_NAME_2 = "swisstour"
COLLECTION_NAME_3 = "viator"

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

    if res.json()['response']['numFound'] > 0:
        for a in res.json()['response']['docs']:
            print(a['title'])
    else:
        print("No documents were found for your query.")