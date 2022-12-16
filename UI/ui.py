from query import query
import pprint
# from PyInquirer import prompt
WEBSITE_1 =  "Get Your Guide"
WEBSITE_2 =  "Swiss Tour"
WEBSITE_3 =  "Viator"


# def pyinquirerUI():
    
#     print("Welcome to an unfirendly web search!")
#     questions = [
#         {
#             'type':'list',
#             'name':'website',
#             'message': 'Which website do you want to search from?',
#             'website':['Swiss Tours','GetYourGuide','Viator']
#         },
#         {
#             'type':'list',
#             'name':'attribute',
#             'message': 'Which attribute do you want to use?',
#             'website':['Title','Description','Price','Rating']
#         }
#     ]
    
#     answers = prompt.prompt(questions)
#     pprint(answers)

def terminalUI():
    
    pp = pprint.PrettyPrinter(indent=4)
    
    seperator = "#"*50 + "\n"
    
    pp.pprint(seperator)
    
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
        print("[1] Title\n")
        print("[2] Price\n")
        print("[3] Description\n")
        print("[4] Rating\n")
        
        choice_attribute = int(input("Choice: "))
    
        
    question = input("What is your query: ")
    query(choice_website, question, choice_attribute)


    
