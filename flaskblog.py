from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f008469d18d7dca519f1ba3150473a8a'

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login',form = form)

if __name__ == '__main__':
    app.run(debug=True)