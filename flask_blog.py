from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'f7f7d158514cccf5854dad96a551147c'

posts = [
    {
        'author': 'Meredith Welch',
        'title': 'Blog Post 1',
        'content': 'This is where the first blog post content will go',
        'date_posted': 'May 25, 2020'
    },
    {
    'author': 'Meredith Welch',
    'title': 'Blog Post 2',
    'content': 'Second blog post content, wahoo',
    'date_posted': 'May 26, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register')
def signup():
    form = RegistrationForm()
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)