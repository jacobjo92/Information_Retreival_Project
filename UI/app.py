from flask import Flask, render_template, url_for, request, redirect
import query as q


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        search_content = request.form['content']
        print(search_content)

        # Need to get the choice of website and attribute to filter for.
        q.query(search_content)
        return redirect('/')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)