import requests
def cleanup_string(input):
    input = input.replace("\n", "")
    return input                    
# UI for querying the localhost.
def query(choice, user_query, attribute):
    
    title = []
    description = []
    price = []
    rating = []
    url = []
    
    
    URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=OR&q="+user_query
    res = requests.get(URL)
    
    if choice != "swisstour":
        if res.json()['response']['numFound'] > 0:
            print("Number of results: " + str(res.json()['response']['numFound']))
            for a in res.json()['response']['docs']:
                if 'description' in a and 'title' in a and 'rating' in a and 'price' in a and 'url' in a:
                    title.append(cleanup_string(str(a['title'][0])))
                    description.append(cleanup_string(str(a['description'][0])))
                    price.append(cleanup_string(str(a['price'][0])))
                    rating.append(cleanup_string(str(a['rating'][0])))
                    url.append(cleanup_string(str(a['url'][0])))
            return title,description,price,rating, url
        else:
            print("No documents were found for your query.")
    else:
        if res.json()['response']['numFound'] > 0:
            print("Number of results: " + str(res.json()['response']['numFound']))
            for a in res.json()['response']['docs']:
                if 'description' in a and 'title' in a and 'price' in a and 'url' in a:
                    title.append(cleanup_string(str(a['title'][0])))
                    description.append(cleanup_string(str(a['description'][0])))
                    price.append(cleanup_string(str(a['price'][0])))
                    url.append(cleanup_string(str(a['url'][0])))
                    rating.append("No rating for swiss tours.")
            return title,description,price,rating, url         
                    
        else:
            print("No documents were found for your query.")