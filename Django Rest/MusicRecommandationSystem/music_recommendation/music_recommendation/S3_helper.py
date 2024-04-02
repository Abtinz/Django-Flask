import logging

import boto3
from botocore.exceptions import ClientError

ENDPOINT_URL = "https://storage.iran.liara.space"
ACCESS_KEY = '6tv0267v5ot0uilr'
SECRET_KEY = '4c34ab62-c877-4022-b0ba-cc2064b12a95'
BUCKET_NAME = 'music-recommander'


# Configure logging
# function to upload file to s3
def upload_to_server(music_file, song_id):
    logging.basicConfig(level=logging.INFO)
    # define the s3 resource
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=ENDPOINT_URL,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    except Exception as exc:
        logging.error(exc)
    else:
        try:
            # upload the file to s3
            bucket = s3_resource.Bucket(BUCKET_NAME)
            bucket.put_object(
                ACL='public-read',
                Body=music_file,
                Key=str(song_id),
            )
            return True
        except ClientError as e:
            logging.error(e)


# function to get the s3 url of the file
def create_song_url(song_id):
    return ENDPOINT_URL + str(song_id)


# function to download the file from s3
# if you want to download the file from s3 you can use this function
# please note that you should have the file in your s3 bucket,
# and you should have the id of the file
# the function will download the file in the /tmp directory
# you can change the download path
# the function will return True if the file is downloaded
# and False if the file is not downloaded
# uncomment the function to use it
def download_from_server(song_id):
    logging.basicConfig(level=logging.INFO)

    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=ENDPOINT_URL,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )
    except Exception as exc:
        logging.error(exc)
    else:
        try:
            bucket = s3_resource.Bucket(BUCKET_NAME)
            download_path = '/tmp/{}'.format(song_id)
            bucket.download_file(create_song_url(song_id), download_path)
            return True
        except ClientError as e:
            logging.error(e)
            return False