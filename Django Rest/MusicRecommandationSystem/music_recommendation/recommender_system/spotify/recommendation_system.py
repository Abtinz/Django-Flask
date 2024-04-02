import requests

'''
    this function will call spotify recommendations engine for given song info
        param -> song information like spotify id
        return -> 
            response: response of api  which will show the song info, nullable for  exception modes!
            message: controller key for state management of exception and successful modes
'''
def spotify_recommendation_system(spotify_song_id, artists, genre):
    
    #recommendations system url
    url = "https://spotify23.p.rapidapi.com/recommendations/"

    #api needed headers like my specify rapidapi key
    headers = {
        "X-RapidAPI-Key": "e18841f4dbmsh57e0490609797f9p12fda6jsne40408af9337",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    #query sets of recommendation engine
    querystring = {
        "limit": "20", 
        "seed_tracks": str(spotify_song_id), 
        "seed_artists": str(artists),
        "seed_genres": str(genre)
    }

    #and now, apocalypse now (api call)
    try:

        response = requests.get(url = url, headers=headers, params=querystring)
        return response.json()  , "successful"

    except Exception as error:
        print(error)
        return None , error

    