from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

# Step 1: Set up your Spotify credentials
CLIENT_ID = "1b447c06b9d54f7799872d85e3845dd4"
CLIENT_SECRET = "e6b30b1535c64d7c84242478b293b7e9"
REDIRECT_URI = "http://localhost:8888/callback"  # You can use localhost for dev

# Step 2: Spotify authorization scope to get liked songs
SCOPE = "user-library-read user-library-modify playlist-modify-public"

# Step 3: Set up Spotipy client (Python library for Spotify API)
spotipy_client = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
    )
)


# Fetch liked songs
def fetch_liked_songs():
    liked_songs = {}

    # multi-page results dictionary
    results = spotipy_client.current_user_saved_tracks(limit=50)

    while results:
        for item in results["items"]:
            track = item["track"]
            liked_songs[track["id"]] = {
                "id": track["id"],
                "title": track["name"],
                "artist": track["artists"][0]["name"],
                "album": track["album"]["name"],
                "release_decade": track["album"]["release_date"][:3] + "0s",
                "added_at": item["added_at"],
            }

        # Pagination - check for next set of songs
        if results["next"]:
            results = spotipy_client.next(results)
        else:
            break

    return liked_songs


# Fetch and store songs in JSON
def save_songs_to_file(song_data, filename="liked_songs.json"):
    with open(filename, "w") as f:
        json.dump(song_data, f, indent=4)


def create_playlist(name, song_ids):
    user_id = spotipy_client.current_user()["id"]
    playlist = spotipy_client.user_playlist_create(user_id, name)

    # Split song_ids into chunks of 100
    chunk_size = 100
    for i in range(0, len(song_ids), chunk_size):
        chunk = song_ids[i : i + chunk_size]
        spotipy_client.playlist_add_items(playlist["id"], chunk)

    return playlist["id"]


# Example usage
organized_songs = {
    "1980s": [{"id": "song_id_1"}, {"id": "song_id_2"}, ...],  # Add actual song IDs
    "1990s": [{"id": "song_id_101"}, {"id": "song_id_102"}, ...],  # Add actual song IDs
}


# Step 7: Organize songs by release decade
def organize_songs_by_decade(liked_songs):
    organized_songs = {}

    for song_id, song_info in liked_songs.items():
        release_decade = song_info["release_decade"]

        if release_decade not in organized_songs:
            organized_songs[release_decade] = []

        organized_songs[release_decade].append(song_info)

    return organized_songs


def create_decade_playlists(organized_songs):
    for decade, songs in organized_songs.items():
        playlist_name = f"{decade} Playlist"
        song_ids = [song["id"] for song in songs]
        playlist_id = create_playlist(playlist_name, song_ids)


def create_monthly_playlists(liked_songs):
    current_year = datetime.now().year
    organized_songs = {}

    for song_id, song_info in liked_songs.items():
        added_year = int(song_info["added_at"].split("-")[0])

        if added_year == current_year:
            added_month = song_info["added_at"].split("-")[1]

            if added_month not in organized_songs:
                organized_songs[added_month] = []

            organized_songs[added_month].append(song_info)

    for month, songs in organized_songs.items():
        month_names = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        playlist_name = f"{month_names[int(month) - 1]} {current_year}"
        song_ids = [song["id"] for song in songs]
        playlist_id = create_playlist(playlist_name, song_ids)


if __name__ == "__main__":
    # Step 6: Fetch songs
    liked_songs = fetch_liked_songs()
    create_monthly_playlists(liked_songs)

    # Step 7: Save to JSON
    # save_songs_to_file(liked_songs)
    # print(f"Saved {len(liked_songs)} liked songs to liked_songs.json")
    # organized_songs = organize_songs_by_decade(liked_songs)
# create_decade_playlists(organized_songs)
