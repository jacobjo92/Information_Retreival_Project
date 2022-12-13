import sys
from query import query
from ui import terminalUI
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')
# app.run()


# def main(app):
#     # terminalUI()
#     webUI(app)
if __name__ == '__main__':
    app.run()
    