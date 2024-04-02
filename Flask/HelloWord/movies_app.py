from flask import Flask
from datasource import movies

app = Flask(__name__)

@app.get("/movies/")
def get_movies():
    return movies

@app.get("/movies/Shawshank/")
def get_shawshenk():
    for movie in movies:
        if movie["Series_Title"] == "The-Shawshank-Redemption":
            return movie
        
@app.get("/movies/<title>")
def get_shawshenk_titled(title):
    for movie in movies:
        if movie["Series_Title"] == title:
            return movie
app.run()