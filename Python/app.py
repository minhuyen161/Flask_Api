from flask import Flask, render_template

app = Flask(__name__)

posts=[
    {
        'author': 'simble',
        'title': 'Fist title',
        'content': 'Fist Content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Brand',
        'title': 'Second title',
        'content': 'Second Content',
        'date_posted': 'April 21, 2018'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html', posts = posts)

@app.route("/about")
def about():
    return render_template('layout.html')
if __name__ == '__main__':
    app.run(debug=True)