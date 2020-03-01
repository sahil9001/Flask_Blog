from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Test post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2019'
    },
    {
        'author': 'Djan Go',
        'title': 'Test post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts, title = 'Home')

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')



if __name__ == '__main__':
    app.run(debug=True)