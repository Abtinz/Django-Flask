import requests

'''
    this api service will help us to find related movies by user queries
    args -> query: this query is supposed to be movie name or related name
'''
def second_service(query):
    
    print("second api process is started ....")
    url = f"https://imdb-search2.p.rapidapi.com/%{query}%7D"

    headers = {
	    "X-RapidAPI-Key": "e18841f4dbmsh57e0490609797f9p12fda6jsne40408af9337",
	    "X-RapidAPI-Host": "imdb-search2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    #lets test our api
    print(second_service("seven"))

