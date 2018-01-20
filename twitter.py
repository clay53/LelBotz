from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def tweet (msg, img = ''):
    if (img):
        photo = open(img, 'rb')
        response = twitter.upload_media(media=photo)
        twitter.update_status(status=msg, media_ids=[response['meadia_id']])
    else:
        twitter.update_status(status=msg)

def search (q, result_type = 'latest'):
    return twitter.search(q=q, result_type=result_type)