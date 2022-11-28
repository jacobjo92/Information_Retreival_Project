import requests
COLLECTION_NAME_1 = "getyourguide"
COLLECTION_NAME_2 = "swisstour"
COLLECTION_NAME_3 = "viator"
URL_1 = "http://localhost:8983/solr/" + COLLECTION_NAME_1 + "query?..."
URL_2 = "http://localhost:8983/solr/" + COLLECTION_NAME_2 + "query?..."
URL_3 = "http://localhost:8983/solr/" + COLLECTION_NAME_3 + "query?..."

# UI for querying the localhost.
def query(choice = 1, user_query = "."):
    URL = "http://localhost:8983/solr/#/gettingstarted/query?q=Test&q.op=OR&indent=true&df=name"
    # if (choice == 1):
    #     URL = URL_1
    # elif (choice == 2):
    #     URL = URL_2
    # elif (choice == 3):
    #     URL = URL_3
    res = requests.get(URL)
    json_response = res.json('response')

    if res['numFound'] > 0:
        # print(json_response)
        ...
    else:
        print("No documents were found for your query.")