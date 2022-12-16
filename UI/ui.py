from query import query
from snakemd import Document
from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
from rich.markdown import Markdown
from rich.style import Style
from PyInquirer import prompt
from reccomender import create_csv



WEBSITE_1 =  'Get Your Guide'
WEBSITE_2 =  'Swiss Tours'
WEBSITE_3 =  'Viator'
RESULT_OUTPUT_PATH ="result"
COLLECTION_NAME_1 = 'getyourguide'
COLLECTION_NAME_2 = 'swisstour'
COLLECTION_NAME_3 = 'viator'

Doc = Document("query")
layout = Layout()
console= Console()
style = Style(bold=True)

n_documents = 0
# context = MarkdownContext(console,options=)

# context.enter_style(style)

console.style= style


def create_md(doc, title,description, price,rating, url):
    doc.add_header(title,1)
    doc.add_header("Description",2)
    doc.add_header(description,3)
    doc.add_header("Price",2)
    doc.add_header(price,3)
    doc.add_header("Rating",2)
    doc.add_header(rating,3)
    doc.add_header("URL",2)
    doc.add_header(url,3)
    
    return doc


def print_snippet_md():
    f = open('result/query.md','r')
    stringmd = f.read()
    md = Markdown(stringmd)
    console.print(md)


def pyinquirerUI():
    intro_text_panel = Panel(Text("Welcome to terminal based web search!", style="bold magenta", justify="center"))
    extra_info_text = Text("There are three avaiable websited to search from: Swiss Tours, Get Your Guide and Viator.\n")
    extra_info_text.append(Text("Viator offer tours from Las Vegas, The Netherlands and Paris.\n"))
    extra_info_text.append(Text("Get Your Guide offer tours from London.\n"))
    extra_info_text.append(Text("Swiss Tours offers tours from Switzerland."))
    
    print(intro_text_panel)
    print(Panel(extra_info_text))
    
    questions = [
        {
            'type':'list',
            'name':'website',
            'message': 'Which website do you want to search from?',
            'choices':['Swiss Tours','GetYourGuide','Viator']
        },
        {
            'type':'list',
            'name':'attribute',
            'message': 'Which attribute do you want to use to filter?',
            'choices':['Title','Description']
        },
        {
            'type':'input',
            'name':'query',
            'message':'What is your query?',
        }
    ]
    
    answers = prompt(questions)
    website = answers['website']
    attribute = answers['attribute']
    user_query = answers['query']
    
    if website == WEBSITE_1:
        website = COLLECTION_NAME_1
    elif website == WEBSITE_2:
        website = COLLECTION_NAME_2
    elif website == WEBSITE_3:
        website = COLLECTION_NAME_3
        
    attribute = attribute.lower()
    
    title, description, price, rating, url =  query(website, user_query, attribute)
    if title != "0":
        
        for i in range(0,len(title)):
            document = create_md(Doc,title[i],description[i],price[i],rating[i], url[i])
        document.output_page(RESULT_OUTPUT_PATH)
        print_snippet_md()
        print(Panel(Text("Number of results: " + str(len(title)))))
        print(Panel(Text("Query results were saved in: {results}".format(results=RESULT_OUTPUT_PATH+"/"+"query.md"))))
    else:
        print(Panel(Text("Number of results: 0")))
        print(Panel(Text("Query results were saved in: {results}".format(results=RESULT_OUTPUT_PATH+"/"+"query.md"))))
    

def terminalUI():
    
    seperator = "#"*50 + "\n"
    print(seperator)
    
    print("Select one of the following:\n")
    print("[1] Get Your Guide\n")
    print("[2] Swiss tours\n")
    print("[3] Viator\n")

    choice_website = int(input("Choice: "))
    choice_attribute = 1
    
    if (choice_website == 1):
        WEBSITE = WEBSITE_1
        print(seperator)
        print("You chose: " + WEBSITE_1+'\n')
        print(seperator)
        print("What search attribute do you want to have?\n")
        print("[0] None\n")
        print("[1] Title\n")
        print("[2] Price\n")
        print("[3] Description\n")
        print("[4] Rating\n")
        choice_attribute = int(input("Choice: "))
    elif (choice_website == 2):
        WEBSITE = WEBSITE_2
        print(seperator)
        print("You chose: " + WEBSITE_2+'\n')
        print(seperator)
        print("What search attribute do you want to have?\n")
        print("[0] None\n")
        print("[1] Title\n")
        print("[2] Price\n")
        print("[3] Description\n")
        print("[4] Included perks\n")
        print("[5] Excluded perks\n")
        choice_attribute = int(input("Choice: "))
    elif (choice_website == 3):
        WEBSITE = WEBSITE_3
        print(seperator)
        print("You chose: " + WEBSITE_3+'\n')
        print(seperator)
        print("Your query will be used for the following locations:\n")
        print("London\n")
        print("Las Vegas\n")
        print("New York\n")
        print("The Netherlands\n")
        print("Paris\n")
        print(seperator)
        print("What search attribute do you want to have?\n")
        print("[0] None\n")
        print("[1] Title\n")
        print("[2] Price\n")
        print("[3] Description\n")
        print("[4] Rating\n")
        
        choice_attribute = int(input("Choice: "))
    
    question = input("What is your query: ")
    query(choice_website, question, choice_attribute)


    
