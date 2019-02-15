from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'SanjayYr',
        'title': 'BlogPost 1',
        'content': 'First Post Content',
        'date': 'February 14, 2019'
    },
    {
        'author': 'SanjayYr2',
        'title': 'BlogPost 2',
        'content': 'Second Post Content',
        'date': 'February 15, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
