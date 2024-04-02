from flask import Flask
from datasource import movies

app = Flask(__name__)

@app.get("/movies/")
def get_movies():
    return "<p>Hello, Flask!!!</p>"

app.run()