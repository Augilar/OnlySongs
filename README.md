<!---
<h1 align="center"> OnlySongs </h1>
--->
<p align = "center">
  <img src="./onlySongs-logos_transparent.png" alt="OnlySongs logo" title="OnlySongs"  height="350" style="display: block; margin: 0 auto" />
</p>

<p> <b>
Hear songs not ads on spotify.
Mutes spotify whenever an ad comes. </b>
</p>
In Ubuntu

How to use it

- create an app in spotify developer dashboard https://developer.spotify.com/dashboard/
- copy the client_id and client_secret
- enter a random working url as redirect uri in the settings (eg: https://localhost:8080/callback)
- now create global variables in the terminal by typing the following,
```
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client_secret'
export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
```
    note - if you don't want to type these commands every time, you can add these to your .bashrc file.

- Then clone the repo
- from the terminal run the ad_muter.py file,
```
python3 ad_muter.py
```

- enjoy spotify without having to listen to ads and buying premium

