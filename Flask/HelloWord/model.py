from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI will set via given url (in memory or cloud paths) in app configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

#ORM Creation vie WSGI configs
db = SQLAlchemy(app= app)