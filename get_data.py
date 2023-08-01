import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pandas as pd

#extract info from env file
load_dotenv()
client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')

#deal with authentication/authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, 
redirect_uri="http://localhost:8888/callback", scope='playlist-read-private user-top-read playlist-modify-private'))

#everything playlist
playlist_link = "https://open.spotify.com/playlist/5jbbLJqtKuqhRENtQFdrqi?si=8018f59b99b44813"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

total_tracks = sp.playlist_tracks(playlist_URI)["total"]
limit = 100
track_data = []
for offset in range(0, total_tracks, limit):
    playlist_tracks = sp.playlist_tracks(playlist_URI, offset=offset, limit=limit)["items"]
    for track in playlist_tracks:
        track_uri = track["track"]["uri"]
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        track_pop = track["track"]["popularity"]

        audio_features = sp.audio_features(track_uri)[0]
        acousticness = audio_features['acousticness']
        danceability = audio_features['danceability']
        energy = audio_features['energy']
        instrumentalness = audio_features['instrumentalness']
        key = audio_features['key']
        loudness = audio_features['loudness']
        mode = audio_features['mode']
        speechiness = audio_features['speechiness']
        tempo = audio_features['tempo']
        time_signature = audio_features['time_signature']
        valence = audio_features['valence']

        track_data.append({
        'Track Name': track_name,
        'Artist Name': artist_name,
        'Popularity': track_pop,
        'Acousticness': acousticness,
        'Danceability': danceability,
        'Energy': energy,
        'Instrumentalness': instrumentalness,
        'Key': key,
        'Loudness': loudness,
        'Mode': mode,
        'Speechiness': speechiness,
        'Tempo': tempo,
        'Time Signature': time_signature,
        'Valence': valence,
        })
df = pd.DataFrame(track_data)
with open('raw_data.txt', 'w') as output:
    output.write('Raw Data:\n')
    output.write(df.to_string(index=False))
