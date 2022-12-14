from flask import Flask, render_template, url_for, request, redirect
import query as q


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        search_content = request.form['content']
        website = request.form['swisstour'], request.form['getyourguide'], request.form['viator']
        attribute = request.form['title'], request.form['description'], request.form[
            'price'], request.form['rating'], request.form['included'], request.form['excluded']
        print(search_content)
        print(website)
        print(attribute)

        # Need to get the choice of website and attribute to filter for.
        # q.query(search_content)
        return redirect('/')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
