#mute the spotify client when an advertisement comes

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import json
import os
import time

scope = ["user-library-read","user-read-currently-playing", "app-remote-control"]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

current_song = sp.currently_playing()

# if current_song["currently_playing_type"] == "track":
#     muted = False
# else:
#     muted = True

muted = False
prev_song = ""
curr_song = ""

while True:

    try:
        current_song = sp.currently_playing()

        if(not muted and current_song["item"] is not None):
            curr_song = current_song["item"]["name"]
        if(not muted and prev_song != curr_song):
            prev_song = curr_song
            print(current_song["currently_playing_type"] + " : " + current_song["item"]["name"] + " : " + current_song["item"]["artists"][0]["name"])
            

        if((muted is False) and (current_song["currently_playing_type"] == "ad")) :
            print(current_song["currently_playing_type"])
            os.system("bash mute.sh")
            muted = True

        if(muted and (current_song["currently_playing_type"] == "track")):
            os.system("bash mute.sh")
            muted = False
        
    except:
        time.sleep(2)




# host = "https://api.spotify.com"
# endpoints = {
#     "current-playing" : "/v1/me/player/currently-playing",
#     "volume" : "/v1/me/player/volume"
# }

# url_track = host + endpoints["current-playing"]
# url_volume = host + endpoints["volume"]

# token = "BQCm-bLoRHHvVv58BCzYyEV07SHqsvOAv6ADF1kgs48Gih2MsDmJKHi7wa8cYkC-4Y9L4cuFYHDj8wLXp1XGvaukUO-D-MYlQSaQQn2KYBGj6XIdV6UQvW4ub3COPQJh1IG5kXhtTxCIsFUkr08VKBg3FPvinLkVs3ZOUzqNiawNT6hvjdp6YEVkJ1tqZdh2WXp4tLIlxF8"

# headers = {
#     "Authorization" : "Bearer "+token,
#     "Content-Type": "application/json",
#     }

# payload = {
#     "volume_percent" : 100,
# }

# response = requests.put(url_track, headers=headers)

# json_resp = json.loads(response.text)

# #track or ad
# #json_resp["currently_playing_type"]

# print(response.text)
