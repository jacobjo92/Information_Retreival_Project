import sys
from query import query
from ui import terminalUI, webUI
from flask import Flask


app = Flask(__name__)
webUI(app)
# app.run()


# def main(app):
#     # terminalUI()
#     webUI(app)
# if __name__ == '__main__':
#     app = Flask(__name__)
#     main(app)
#     app.run()
    