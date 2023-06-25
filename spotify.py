import spotipy
from spotipy.oauth2 import SpotifyOAuth
from createplaylist import CreatePlay
from pprint import pprint

date = input("Enter the year to which you want to travel in YYYY-MM-DD : ")
URL = f"https://www.billboard.com/charts/hot-100/{date}/"
playlist = CreatePlay().create(URL)

SPOTIFY_ENDPOINT = "https://api.spotify.com/v1/users/"
SPOTIFY_CLIENT_ID = "<Your Spotify Client ID>"   #You need to have a spotify account in developer.spotify.com where you will get an access token along with Client ID and a Secret Key
SPOTIFY_CLIENT_SECRET = "Spotify Client Secret Key"
USERNAME = "Your Username"
URL_REDIRECTED = "http://127.0.0.1:8080/?code=AQAsdz96QqTZF61kJtmgWTBE6q3DPpdan4ceDLWQMhiaQ8Ze5hpAVeOLUBKggPAu3Akxu1M5C5xqQFt58cZBwUqRaA7rASh-woQHgUHZJlvu90zbTGPLMepzrKK2r4kJVi28sJfpKThJcZq4BG4A507V0Z5zS_Oy0fnS_p8-yBrgKjORokVuOh9EKBrTBP64Zn8"

header = {
    "Authorization": "Bearer " + SPOTIFY_CLIENT_SECRET
}

response = SpotifyOAuth(
                    client_id=SPOTIFY_CLIENT_ID,
                    client_secret=SPOTIFY_CLIENT_SECRET,
                    redirect_uri='http://127.0.0.1:8080',
                    scope="playlist-modify-private",
                    show_dialog=True,
                    cache_path="token.txt"
                )

sp = spotipy.Spotify(auth_manager=response)

user_id = sp.current_user()["id"]

song_URI = []
playlist_name = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False)
year = date.split('-')[0]
for index, song_name in enumerate(playlist):
    try:
        result_uri = sp.search(q=f"track: {song_name} year: {year}", type='track')
        song_URI.append(result_uri['tracks']['items'][0]['uri'])
    except:
        print(f"Song {song_name} not available")

sp.playlist_add_items(playlist_id=playlist_name["id"], items=song_URI)
print("Playlist created successfully!")



