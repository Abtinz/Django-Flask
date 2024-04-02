import requests

'''
    this function will help us to call shezam api for song recognition 
        param -> song_url: this url is our considered song file address in s3 cloud server
        return -> a list of predicted  songIds
'''
def shezam_api(song_url):

    #shezam recognize api url
    url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"

    #headers of api call(specified by rapidapi for shazam )
    headers = {
	    "content-type": "multipart/form-data; boundary=---011000010111000001101001",
	    "X-RapidAPI-Key": "e18841f4dbmsh57e0490609797f9p12fda6jsne40408af9337",
	    "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
    }

    #in this payload we will show the shezam api service our song url
    payload = f"-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"{song_url}\"\r\n\r\n\r\n-----011000010111000001101001--\r\n\r\n"

    response = requests.post(url = url, data=payload, headers=headers)

    return response.json()
