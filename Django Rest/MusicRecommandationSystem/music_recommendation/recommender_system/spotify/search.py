import requests

'''
    this function will call spotify search engine for given song name
        param -> song_name: given name of song from shezam service for given song file
        return -> 
            response: response of api  which will show the song id for next service, nullable for not found and exception modes!
            message: controller key for state management of exception and successful modes
'''
def spotify_search_engine(song_name):

    #search engine url
    url = "https://spotify23.p.rapidapi.com/search/"

    #here we specify our querysets for api like query parameter(song name)
    querystring = {
        "q": song_name, 
        "type": "tracks", 
        "offset": "0", 
        "limit": "1", 
        "numberOfTopResults": "10"
    }

    #headers of api like my rapidapi key
    headers = {
        "X-RapidAPI-Key": "e18841f4dbmsh57e0490609797f9p12fda6jsne40408af9337",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    #and now, apocalypse now (api call)
    try:
        response = requests.get(url = url, headers=headers, params=querystring).json().get("tracks", {}).get("items", [])
        if response:
            return response[0].get("id") , "successful"
        else:
            return None , "empty"
    except Exception as error:
        print(error)
        return None , error

    