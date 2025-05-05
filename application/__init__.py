from flask import Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
#from flask_login import LoginManager


app = Flask(__name__)

# Load existing config (if any)
#app.config.from_pyfile('config.py', silent=True) 

app.config['SECRET_KEY'] = 'bhakundo-nepal'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soccerDB.db'
# app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///soccerDB.db'

app.config['SQLALCHEMY_BINDS'] = {
        'users': 'sqlite:///usersDB.db',       # For auth (optional)
        'primary': 'sqlite:///soccerDB.db'   # Your existing DB (if different)
    }
#login_manager = LoginManager()

db = SQLAlchemy(app)


from application import routes, models
