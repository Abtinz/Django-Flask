import json
from flask import Flask, abort, request, jsonify
from elasticsearch_service import *
from redis_service import RedisCacheSystem
from second_service import second_service

app = Flask(__name__)

@app.route('/movies/search', methods=['GET'])
def search_query():

    try:

        query = request.args.get('query')
        
        if query is None:
            return abort(400,{'message': 'bad request caused by incorrect and incomplete request queries'})
        
        redis_info = cache_system.find(query)

        if redis_info :
            return jsonify(
                    {
                        'result': json.loads(redis_info) , 
                        'message': "this information is extracted from redis and cache service"
                }), 200
        else:
            print("redis does not have needed data for this query ...\n elasticsearch process is started")

            #now we need to search through elasticsearch system
            
            elasticsearch_info = search_system.search(query)
            print(elasticsearch_info)
            if elasticsearch_info and len(elasticsearch_info) != 0:
                cache_system.add(query, json.dumps(elasticsearch_info))
                return jsonify(
                    {
                        'result': elasticsearch_info , 
                        'message': "this information is extracted from elasticsearch service"
                }) , 200
            
            else:
                #now we have to call our second api
                api_info = second_service(query)

                if api_info and len(api_info) != 0:
                    cache_system.add(query, json.dumps(api_info))
                    return jsonify(
                    {
                        'result': api_info , 
                        'message': "this information is extracted from api.imdb service"
                }) , 200
            
            return abort(404,{'message': 'no results for given name in imdb, elasticsearch system and redis'})


    except Exception as error:
        print(error)
        try:
            #we may have problems in redis or elasticsearch services
            api_info = second_service(query)

            if api_info and len(api_info) != 0:
                    cache_system.add(query, json.dumps(api_info))
                    return jsonify(
                    {
                        'result': api_info , 
                        'message': "this information is extracted from api.imdb service"
            }) , 200

            return abort(404,{'message': 'no results for given name in imdb, elasticsearch system and redis'})

        except Exception as error2:

            print(error2)
            return abort(500,{'message': str(error)})
        

if __name__ == '__main__':
    
    #initializing the redis cache system and elastic database, then we will run flask app on 0.0.0.0:5000(no need to debug mode)
    cache_system = RedisCacheSystem()
    search_system = ElasticSearchService()
    app.run(debug=False, host='0.0.0.0', port=5000)