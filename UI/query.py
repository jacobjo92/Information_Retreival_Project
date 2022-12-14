import requests
def cleanup_string(input):
    input = input.replace("\n", "")
    return input                    
# UI for querying the localhost.
def query(choice, user_query, attribute, max_price):
    
    title = []
    description = []
    price = []
    rating = []
    url = []
    URL = ""
    if user_query == "" and max_price == "":
        URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=AND&q=*:*"    
    if user_query == "" and max_price != "":
        URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=AND&q=price:" +"[* TO "+ max_price+"]"
    if user_query != "" and max_price != "":
        URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=AND&q="+attribute+":"+user_query + " price:" +"[* TO "+ max_price+"]"
    if user_query != "" and max_price == "":
        URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=AND&q="+attribute+":"+user_query

    res = requests.get(URL)
    zero = "0"
    
    if choice != "swisstour":
        if res.json()['response']['numFound'] > 0:
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
            return zero,zero,zero,zero,zero
    else:
        if res.json()['response']['numFound'] > 0:
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
            return zero,zero,zero,zero,zero
        
        
# def recommend(choice, user_query_analysis, attribute):
#     URL = "http://localhost:8983/solr/#/"+choice+"/analysis?analysis.query=Cocktails&analysis.fieldtype=text_en&verbose_output=1"
#     res = requests.get(URL)
#     print(res.json())