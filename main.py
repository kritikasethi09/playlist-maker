import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
redirect_uri = os.environ.get('REDIRECT_URI')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, 
redirect_uri="http://localhost:8888/callback", scope='playlist-read-private'))
def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']

    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    return tracks


playlist_id = '5jbbLJqtKuqhRENtQFdrqi'
tracks = get_playlist_tracks(playlist_id)
for idx, track in enumerate(tracks, start=1):
    track_name = track['track']['name']
    track_artist = track['track']['artists'][0]['name']
    print(f"{idx}. {track_name} - {track_artist}")