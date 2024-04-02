from celery import shared_task

from music_recommendation.mailgun import mailgun_service
from recommender_system.spotify.recommendation_system import spotify_recommendation_system
from shezam_service.shezam import shezam_api
from song_registration.models import SongRequests

@shared_task
def process_music_recognition(request_id):
    global music_request
    try:
        print(request_id)
        music_request = SongRequests.objects.get(id=request_id) 
        spotify_id = shezam_api(music_request.audio_file.path)
        print(spotify_id)
        music_request.song_id = spotify_id
        music_request.status = 'ready'
        music_request.save()
        process_recommendations.delay()

    except Exception as error:
        music_request.status = 'failure'
        music_request.save()
        raise error

def format_recommendations(recommendations):
    message = "Here are your music recommendations:\n\n"
    for idx, rec in enumerate(recommendations['tracks'], start=1):
        artists = ', '.join(artist['name'] for artist in rec['artists'])
        message += f"{idx}. {rec['name']} by {artists}\n"
    return message


@shared_task
def process_recommendations():
    ready_requests = SongRequests.objects.filter(status='ready')
    for music_request in ready_requests:

        recommendations = spotify_recommendation_system(music_request.song_id, "", "")
        print(recommendations)
        music_request.status = 'done'
        music_request.save()
        

def music_recognition(request_id):
    global music_request
    try:
        print(request_id)
        music_request = SongRequests.objects.get(id=request_id) 
        spotify_id = shezam_api(music_request.song_url)
        print(spotify_id)
        music_request.song_id = spotify_id
        music_request.status = 'ready'
        music_request.save()
        recommendations()

    except Exception as error:
        music_request.status = 'failure'
        music_request.save()
        raise error


def recommendations():
    ready_requests = SongRequests.objects.filter(status='ready')
    for music_request in ready_requests:

        recommendations = spotify_recommendation_system(music_request.song_id, "", "")
        if recommendations:
            music_request.status = 'done'
            music_request.save()
        else:
           music_request.status = 'failure'
           music_request.save() 
            

        