import numpy as np
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
   
username = 'lainiebrown4'
playlist_id = '3A3Z9f1jlhQyl1HXisuieR'

results = sp.user_playlist(username, playlist_id, 'tracks')

playlist_tracks_data = results['tracks']
playlist_tracks_id = []
playlist_tracks_titles = []
playlist_date_released = []
playlist_tracks_artists = []
playlist_tracks_first_artists = []

for track in playlist_tracks_data['items']:
    playlist_tracks_id.append(track['track']['id'])
    playlist_tracks_titles.append(track['track']['name'])
    artist_list = []
    for artist in track['track']['artists']:
        artist_list.append(artist['name'])
    playlist_tracks_artists.append(artist_list)
    playlist_tracks_first_artists.append(artist_list[0])

for uri in playlist_tracks_id:
    track = sp.track(uri)
    playlist_date_released.append(track['album']['release_date'])

features = sp.audio_features(playlist_tracks_id)

features_df = pd.DataFrame(data=features, columns=features[0].keys())

features_df['title'] = playlist_tracks_titles
features_df['artist'] = playlist_tracks_first_artists
features_df['date_released'] = playlist_date_released
features_df['company'] = 'YG'
features_df = features_df[['id', 'title', 'artist', 'company','date_released',
                           'danceability', 'energy', 'key', 'loudness',
                           'mode', 'speechiness', 'acousticness', 'instrumentalness',
                           'liveness', 'valence', 'tempo',
                           'duration_ms']]

features_df.to_csv('treasure.csv')

