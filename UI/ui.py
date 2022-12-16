from query import query
from snakemd import Document
from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.layout import Layout
from rich.prompt import Prompt
from rich.markdown import Markdown, MarkdownContext
from rich.style import Style
from PyInquirer import prompt
WEBSITE_1 =  'Get Your Guide'
WEBSITE_2 =  'Swiss Tours'
WEBSITE_3 =  'Viator'
RESULT_OUTPUT_PATH ="result"
COLLECTION_NAME_1 = 'getyourguide'
COLLECTION_NAME_2 = 'swisstour'
COLLECTION_NAME_3 = 'viator'


console= Console()
style = Style(bold=True)
# context = MarkdownContext(console,options=)

# context.enter_style(style)

console.style= style


def create_md(doc, title,description, price,rating):
    doc.add_header(title,1)
    doc.add_header("Description",2)
    doc.add_header(description,3)
    doc.add_header("Price",2)
    doc.add_header(price,3)
    doc.add_header("Rating",2)
    doc.add_header(rating,3)
    
    return doc


def print_snippet_md():
    f = open('result/query.md','r')
    stringmd = f.read()
    md = Markdown(stringmd)
    console.print(md)


def pyinquirerUI():
    
    # layout = Layout()
    # layout.split_column(
    #     Layout(name="upper"),
    #     Layout(name="lower")
    # )
    intro_text_panel = Panel(Text("Welcome to terminal based web search!", style="bold magenta", justify="center"))
    print(intro_text_panel)
    
    # layout["upper"].size = 5
    # layout["lower"].size = 5
    # layout["lower"].visible = False
    # layout["upper"].update(
    #     intro_text_panel
    # )
    
    # print(layout)
    
    
    
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
            'choices':['Title','Description','Price','Rating']
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
    Doc = Document("query")
    title, description, price, rating =  query(website, user_query, attribute)
    for i in range(0,len(title)):
        document = create_md(Doc,title[i],description[i],price[i],rating[i])
        document.output_page(RESULT_OUTPUT_PATH)
    print(Panel(Text("Query results were saved in: {results}".format(results=RESULT_OUTPUT_PATH+"/"+"query.md"))))
    print_snippet_md()
    

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


    
