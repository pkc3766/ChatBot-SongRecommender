from flask import Blueprint,request
import os
from dotenv import load_dotenv,find_dotenv
songs = Blueprint('songs', __name__)
import requests

toneWithTagMap={
    'Joy':'joy',
    'Sadness':'motivational',
    'Analytical':'instrumental',
    'Anger':'chillout',
    'Fear':'motivational',
    'Confident':'rock',
    'Tentative':'acoustic',
    'Neutral':'experimental'
}

load_dotenv(find_dotenv())

tone='Neutral'

# returns songs with a particular tag(found using tone)
@songs.route('/api/songs',methods=['GET','POST'])
def getSongs():
    # tone=request
    tone='Neutral'
    if request.method=='POST':
        data=request.get_json()
        tone=data['tone']
    # print(tone)
    # print('in getSongs ',tone)
    tag=toneWithTagMap[tone]
    params={
        'api_key':os.environ.get("API_KEY"),
        'limit':5,
        'method':'tag.getTopTracks',
        'tag':tag,
        'format':'json'
    }
    res = requests.post('http://ws.audioscrobbler.com/2.0', params=params)
    songs={}
    for val in res.json()['tracks']['track']:
        songs[val['name']]=[val['url'],val['artist']['name']]
    return songs
    # return res.json()

# returns similar songs to the provided track
@songs.route('/api/songs/similar',methods=['GET','POST'])
def getSimilarSongs():
    track='Ray of Light'
    artist='Madonna'
    if request.method=='POST':
        data=request.get_json()
        track=data['track']
        artist=data['artist']
    params={
        'api_key':os.environ.get("API_KEY"),
        'limit':5,
        'method':'track.getSimilar',
        'track':track,
        'artist':artist,
        'format':'json'
    }
    res = requests.post('http://ws.audioscrobbler.com/2.0', params=params)
    # print(res.json())
    songs={}
    for val in res.json()['similartracks']['track']:
        songs[val['name']]=val['url']
    return songs