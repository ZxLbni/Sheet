import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests

# Spotify API credentials (replace with your own credentials)
CLIENT_ID = 'b9c2df50c0df4676bb9c8525d8dc586b'
CLIENT_SECRET = 'd859816a46bb412eafd716d9056629bd'

# Authenticate with Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Streamlit app
st.title("Spotify Track Search")

# Input for track URL
track_url = st.text_input("Enter Spotify Track URL", "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC")

if track_url:
    try:
        track_id = track_url.split("/")[-1]
        track_info = sp.track(track_id)
        st.subheader("Track Information")
        st.write(f"**Track Name:** {track_info['name']}")
        st.write(f"**Artist:** {', '.join(artist['name'] for artist in track_info['artists'])}")
        st.write(f"**Album:** {track_info['album']['name']}")
        st.write(f"**Release Date:** {track_info['album']['release_date']}")
        st.write(f"**Track URL:** [Click here]({track_url})")
    except Exception as e:
        st.error("Failed to retrieve track info. Please check the URL.")
        st.error(str(e))

# Search functionality with query parameter
query = st.text_input("Search for Tracks", "")
if query:
    results = sp.search(q=query, limit=5, type="track")
    if results["tracks"]["items"]:
        st.subheader("Search Results")
        for idx, track in enumerate(results["tracks"]["items"]):
            st.write(f"{idx + 1}. **{track['name']}** by {', '.join(artist['name'] for artist in track['artists'])}")
            st.write(f"Album: {track['album']['name']} | Release Date: {track['album']['release_date']}")
            st.write(f"[Listen Here]({track['external_urls']['spotify']})")
    else:
        st.write("No results found.")
        
