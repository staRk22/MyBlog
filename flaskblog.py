from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)  # __name__=='__main__'

app.config['SECRET_KEY'] = '262892ca4d1fa437ac16827c4389361f'  # Used secrets.token_hex(16) in cmd to generate this.

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f"You have been logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash(f"logged in failed. Please check username and password", 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
