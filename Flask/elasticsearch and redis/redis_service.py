import os
import redis

'''
    this class will implement redis cache system for our better performances
    properties -> cache : this property will save our redis class with its host and ports
'''
class RedisCacheSystem:
    def __init__(self):
        redis_host = os.environ.get('REDIS_HOST', 'localhost') 
        self.cache = redis.Redis(host=redis_host, port=6379)
        print(f'redis is ready on {redis_host}:6379')

    def find(self, query):
        print(f"redis is searching for {query}")
        return self.cache.get(query)
        

    def add(self, query, value):
        print(f"redis is saving this query:{query}")
        self.cache.set(query, value)

    def clear(self):
        self.cache.flushdb()
        print("redis is cleared and empty")

