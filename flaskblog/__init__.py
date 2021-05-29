from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # __name__=='__main__'
app.config['SECRET_KEY'] = '262892ca4d1fa437ac16827c4389361f'  # Used secrets.token_hex(16) in cmd to generate this.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
