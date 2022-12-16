import requests
from snakemd import Document
from termcolor import colored
from rich.console import Console
from rich.markdown import Markdown
import markdown
COLLECTION_NAME_1 = "getyourguide"
COLLECTION_NAME_2 = "swisstour"
COLLECTION_NAME_3 = "viator"
RESULT_OUTPUT_PATH ="result"
SEARCH_ATTRIBUTE = "title"

def create_md(doc, title,description, price,rating):
    doc.add_header(title)
    doc.add_paragraph(description)
    doc.add_paragraph(price)
    doc.add_paragraph(rating)
    
    return doc


def print_snippet(title,description, price,rating):
    console= Console()
    f = open('result/query.md','r')
    stringmd = f.read()
    md = Markdown(stringmd)
    console.print(md)

def cleanup_string(input):
    input = input.replace("\n", "")
    return input

# UI for querying the localhost.
def query(choice, user_query, attribute):
    
    URL = "http://localhost:8983/solr/" + choice + "/select?df="+attribute+"&indent=true&q.op=OR&q="+user_query
    

    res = requests.get(URL)
    Doc = Document("query")
    if res.json()['response']['numFound'] > 0:
        print("Number of results: " + str(res.json()['response']['numFound']))
        for a in res.json()['response']['docs']:
            if 'description' in a and 'title' in a and 'rating' in a and 'price' in a:
                title = cleanup_string(str(a['title'][0]))
                description = "Description: " + cleanup_string(str(a['description'][0]))
                price = "Price: " + cleanup_string(str(a['price'][0]))
                rating = "Rating: " + cleanup_string(str(a['rating'][0]))
                document = create_md(Doc,title,description,price,rating)
                document.output_page(RESULT_OUTPUT_PATH)
                print_snippet(title,description,price,rating)
                    
                    
    else:
        print("No documents were found for your query.")