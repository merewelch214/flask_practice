from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)