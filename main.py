from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

# User inputs the year they'd like to travel to in YYYY-MM-DD format
date_string = input("Please enter the year you would like to travel to in YYYY-MM-DD format: ")
year = date_string.split("-")[0]  # Extract the year for use in song searches

# Scrape Billboard 100 based on the provided date
url = f"https://www.billboard.com/charts/hot-100/{date_string}"
response = requests.get(url)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
songs = soup.find_all('h3', class_='a-no-trucate', limit=100)
song_titles = [song.get_text(strip=True) for song in songs]

# Authenticate with Spotify
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = 'http://example.com'
scope = 'playlist-modify-private'

auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Create a private playlist for the user
user_id = sp.current_user()['id']
playlist = sp.user_playlist_create(user_id, f"Billboard Top 100 from {date_string}", public=False)
print("Created playlist:", playlist['name'])

# Search for each song on Spotify and add to the playlist if found
track_uris = []
for title in song_titles:
    try:
        result = sp.search(q=f"track:{title} year:{year}", type="track", limit=1)
        track_uri = result['tracks']['items'][0]['uri']
        track_uris.append(track_uri)
    except IndexError:
        print(f"Not found on Spotify: {title}")

# Add tracks to the new playlist
if track_uris:
    sp.playlist_add_items(playlist['id'], track_uris)
    print(f"Added {len(track_uris)} tracks to the playlist.")
else:
    print("No tracks were added to the playlist.")

# Optionally, pprint the list of found URIs for better visualization
pprint(track_uris)
