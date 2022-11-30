import sys
import ui
from query import query
# import query
from PyQt5.QtWidgets import QApplication

WEBSITE_1 =  "Get Your Guide"
WEBSITE_2 =  "Swiss Tour"
WEBSITE_3 =  "Viator"

def main():
    
    app = QApplication(sys.argv)
    window = ui.Window()
    sys.exit(app.exec_())
    
    print("Select one of the following:\n")
    print("[1] Get Your Guide\n")
    print("[2] Swiss tours\n")
    print("[3] Viator\n")

    choice = int(input("Choice: "))
    
    if (choice == 1):
        print("You chose: " + WEBSITE_1+'\n')
    elif (choice == 2):
        print("You chose: " + WEBSITE_2+'\n')
    elif (choice == 3):
        print("You chose: " + WEBSITE_3+'\n')
        
    question = input("What is your query: ")
    query(choice, question)

if __name__ == '__main__':
    main()
    