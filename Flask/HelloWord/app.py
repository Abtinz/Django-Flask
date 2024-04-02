from flask import Flask

#lets create an instance of this class, we are specifying our app rout to wsgi with __name__ which is our file name
app = Flask(__name__)

@app.route("/hello/flask/")
def hello_flask():
    return "<p>Hello, Flask!!!</p>"

app.run()