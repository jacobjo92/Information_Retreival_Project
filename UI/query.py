import requests
import json
from snakemd import Document
COLLECTION_NAME_1 = "getyourguide"
COLLECTION_NAME_2 = "swisstour"
COLLECTION_NAME_3 = "viator"
RESULT_OUTPUT_PATH ="result"
SEARCH_ATTRIBUTE = "title"


def create_md_swiss(doc, title,description, price,inclusions, exclusions,to_know):
    doc.add_header(title)
    doc.add_paragraph(description)
    doc.add_paragraph(inclusions)
    doc.add_paragraph(exclusions)
    doc.add_paragraph(price)
    doc.add_paragraph(to_know)
    
    return doc

def create_md_get_your_guide(doc, title,description, price,rating, provider):
    doc.add_header(title)
    doc.add_paragraph(description)
    doc.add_paragraph(provider)
    doc.add_paragraph(price)
    doc.add_paragraph(rating)
    
    return doc

def create_md_viator(doc, title,description, price,rating):
    doc.add_header(title)
    doc.add_paragraph(description)
    doc.add_paragraph(price)
    doc.add_paragraph(rating)
    
    return doc
    
    

def cleanup_string(input):
    input = input.replace("\n", "")
    return input

# UI for querying the localhost.
def query(choice = 1, user_query = "*%3A*", choice_attribute = 1):
    
    
    if choice_attribute == 1:
        SEARCH_ATTRIBUTE = "title"
    elif choice_attribute == 2:
        SEARCH_ATTRIBUTE = "price"
    elif choice_attribute == 3:
        SEARCH_ATTRIBUTE = "description"
    elif choice_attribute == 4 and choice != 2:
        SEARCH_ATTRIBUTE = "rating"
    elif choice_attribute == 4 and choice == 2:
        SEARCH_ATTRIBUTE = "inclusions"
    elif choice_attribute == 5 and choice == 3:
        SEARCH_ATTRIBUTE = "exclusions"
        
        
    URL_1 = "http://localhost:8983/solr/" + COLLECTION_NAME_1 + "/select?df="+SEARCH_ATTRIBUTE+"&indent=true&q.op=OR&q="+user_query
    URL_2 = "http://localhost:8983/solr/" + COLLECTION_NAME_2 + "/select?df="+SEARCH_ATTRIBUTE+"&indent=true&q.op=OR&q="+user_query
    URL_3 = "http://localhost:8983/solr/" + COLLECTION_NAME_3 + "/select?df="+SEARCH_ATTRIBUTE+"&indent=true&q.op=OR&q="+user_query
    
    
    if (choice == 1):
        URL = URL_1
        res = requests.get(URL)
        Doc = Document("Results of Get Your Guide query")
        if res.json()['response']['numFound'] > 0:
            print("Number of results: " + str(res.json()['response']['numFound']))
            for a in res.json()['response']['docs']:
                if 'description' in a and 'title' in a and 'rating' in a and 'price' in a and 'provider' in a:
                    title = cleanup_string(str(a['title'][0]))
                    description = "Description: " + cleanup_string(str(a['description'][0]))
                    price = "Price: " + cleanup_string(str(a['price'][0]))
                    rating = "Rating: " + cleanup_string(str(a['rating'][0]))
                    provider = "Provider: " + cleanup_string(str(a['provider'][0]))
                    document = create_md_get_your_guide(Doc,title,description,price,rating, provider)
                    document.output_page(RESULT_OUTPUT_PATH)
                    print(document)
                    
        else:
            print("No documents were found for your query.")
    elif (choice == 2):
        URL = URL_2
        res = requests.get(URL)
        Doc = Document("Results of Swiss Tour query")
        
        
        # TODO: Handle empty keys, or just write empty string at empty key.
        
        if res.json()['response']['numFound'] > 0:
            print("Number of results: " + str(res.json()['response']['numFound']))
            for a in res.json()['response']['docs']:
                if 'description' in a and 'title' in a and 'price' in a and 'inclusions' in a and 'exclusions' in a and 'know_before_you_go' in a:
                    title = cleanup_string(str(a['title'][0]))
                    description = "Description: " + cleanup_string(str(a['description'][0]))
                    inclusions = "Included in the tour: " + cleanup_string(str(a['inclusions'][0]))
                    exclusions = "Excluded from the tour: " + cleanup_string(str(a['exclusions'][0]))
                    price = "Price: " + cleanup_string(str(a['price'][0]))
                    to_know = "Things to know: " + cleanup_string(str(a['know_before_you_go'][0]))
                    document = create_md_swiss(Doc,title,description,price, inclusions, exclusions, to_know)
                    document.output_page(RESULT_OUTPUT_PATH)
                    print(document)
        else:
            print("No documents were found for your query.")
            
    elif (choice == 3):
        URL = URL_3
        res = requests.get(URL)
        Doc = Document("Results of Viator query")
        if res.json()['response']['numFound'] > 0:
            print("Number of results: " + str(res.json()['response']['numFound']))
            for a in res.json()['response']['docs']:
                if 'description' in a and 'title' in a and 'rating' in a and 'price' in a:
                    title = cleanup_string(str(a['title'][0]))
                    description = "Description: " + cleanup_string(str(a['description'][0]))
                    price = "Price: " + cleanup_string(str(a['price'][0]))
                    rating = "Rating: " + cleanup_string(str(a['rating'][0]))
                    document = create_md_viator(Doc,title,description,price,rating)
                    document.output_page(RESULT_OUTPUT_PATH)
                    print(document)
            
            
        else:
            print("No documents were found for your query.")