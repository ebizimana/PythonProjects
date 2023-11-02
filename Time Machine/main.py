import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# Parse the billboard website
# year = 2001-09-01
date = input("Which year do you want ot travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

# Scrape the billboard website
songs_tag = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
songs_name = [song.getText().strip() for song in songs_tag]

# Get the songs urls
scope = "user-library-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
))
user_id = sp.current_user()["id"]
year = date.split("-")[0]
songs_url = []
for song in songs_name[:10]:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        song_url = result["tracks"]["items"][0]["external_urls"]
        songs_url.append(song_url["spotify"])
        print(song_url)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create a playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_url)
