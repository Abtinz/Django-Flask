import json
from flask import Flask, abort, request, jsonify

from postgres import PostgresService


app = Flask(__name__)

@app.route('/api/tables/create', methods=['GET'])
def create_tables():

    try:
        postgresService.create_table()
        return jsonify(200, {'message': 'database is created successfully'} )

    except Exception as error:
        return abort(500,{'message': f'connection failed in database system {error}'})

        

if __name__ == '__main__':
    #initializing the postgres database system
    postgresService = PostgresService()
    app.run(debug=False, host='0.0.0.0', port=5000)