from elasticsearch import Elasticsearch

ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = '12345'

'''
    this class will implement our elasticsearch service
    make sure that this command is processed in cmd:
        curl -XPOST -k -u elastic:12345 "https://localhost:9200/_bulk?pretty" -H "Content-Type: application/json" --data-binary @movies.json
''' 
class ElasticSearchService:
    def __init__(self):
        print(f"connected to elasticsearch service")

    def search(self, name):
        
        client = Elasticsearch('https://localhost:9200',http_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),verify_certs=False)
        res = client.search(index="your_index_name", query={
            "match": {
                "Series_Title": name
            }
        })
        client.close()
        return res['hits'], res['hits']['hits']
    
