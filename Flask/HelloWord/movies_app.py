from flask import Flask, abort, request
from datasource import movies, titles

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
def get_titled(title):
    for movie in movies:
        if movie["Series_Title"] == title:
            return movie
    #not fount error
    return abort(404)

@app.post("/movies/new/title/")
def post_new_title():

    json_request = request.json
    print(json_request)
    titles.append(json_request["title"])
    print(titles)
    return json_request

@app.put("/movies/update/<title>")
def put_title(title):
    
    print(title , request.json)
    for movie in movies:
        if movie["Series_Title"] == title:
            movie["Series_Title"] = request.json["title"]
            movie["Released_Year"] = request.json["year"]
            movie["Certificate"] = request.json["certificate"]
            return movie , 201
    
    return abort(404)


app.run()