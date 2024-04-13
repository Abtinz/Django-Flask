from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI will set via given url (in memory or cloud paths) in app configs
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
app.config["SQLALCHEMY_ECH"] = True

#ORM Creation vie WSGI configs
db = SQLAlchemy(app= app)

class Movie(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    cast = db.Column(db.String(400), nullable = True)
    rate = db.Column(db.Float, default = 50)

    def as_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "cast" : self.cast,
            "rate" : self.rate
        }

@app.get("/movies/")
def get_movies():
    return Movie.query.get()

@app.post("/movies/new/")
def post_new_movie():

    json_request = request.json
    print(json_request)
    titles.append(json_request["title"])
    print(titles)
    return json_request

with app.app_context():
    db.create_all()

app.run()

