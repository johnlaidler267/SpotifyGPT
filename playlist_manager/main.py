from auth import get_spotify_client
from fetch_songs import fetch_liked_songs
from playlists import create_monthly_playlists, create_decade_playlists
from utils import save_songs_to_file, organize_songs_by_decade

if __name__ == "__main__":
    spotify_client = get_spotify_client()

    # Fetch liked songs
    liked_songs = fetch_liked_songs(spotify_client)

    # Save to JSON
    save_songs_to_file(liked_songs)

    # Organize by decade and create decade playlists
    organized_songs_by_decade = organize_songs_by_decade(liked_songs)
    create_decade_playlists(spotify_client, organized_songs_by_decade)

    # Create monthly playlists
    create_monthly_playlists(spotify_client, liked_songs)
