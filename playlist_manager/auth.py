from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

from config.settings import REDIRECT_URI, SCOPE, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_spotify_client():
    """
    Initialize and return a Spotipy client authenticated with OAuth credentials.

    Returns:
        Spotify: An authenticated Spotipy client object.
    """
    return Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIFY_CLIENT_ID,
            client_secret=SPOTIFY_CLIENT_SECRET,
            redirect_uri=REDIRECT_URI,
            scope=SCOPE,
        )
    )
