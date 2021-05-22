from flask import Flask, render_template, url_for
app = Flask(__name__)  # __name__=='__main__'

posts = [
    {
        'author': 'Barun Sharma',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'May 21, 2021'
    },
    {
        'author': 'Coery Schafer',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 22, 2021'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
