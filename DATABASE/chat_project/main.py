import json
from flask import Flask, abort, request, jsonify


app = Flask(__name__)

@app.route('/api/initialization', methods=['GET'])
def initialization():

    try:

        
            return abort(404,{'message': 'no results for given name in imdb, elasticsearch system and redis'})


    except Exception as error:
        

        return abort(404,{'message': 'no results for given name in imdb, elasticsearch system and redis'})

        

if __name__ == '__main__':
    
    #initializing the postgres database system
    
    app.run(debug=False, host='0.0.0.0', port=5000)