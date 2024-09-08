import datetime


def create_playlist(spotify_client, name, song_ids):
    """
    Creates a playlist on Spotify with the given name and adds songs to it.

    Args:
        spotify_client (Spotify): An authenticated Spotipy client.
        name (str): The name of the playlist to be created.
        song_ids (list): A list of Spotify track IDs to be added to the playlist.

    Returns:
        str: The ID of the created playlist.
    """
    user_id = spotify_client.current_user()["id"]
    playlist = spotify_client.user_playlist_create(user_id, name)

    # Split song_ids into chunks of 100 to comply with Spotify API limitations
    chunk_size = 100
    for i in range(0, len(song_ids), chunk_size):
        chunk = song_ids[i : i + chunk_size]
        spotify_client.playlist_add_items(playlist["id"], chunk)

    return playlist["id"]


def create_decade_playlists(spotify_client, organized_songs):
    """
    Creates playlists based on song release decades.

    Args:
        spotify_client (Spotify): An authenticated Spotipy client.
        organized_songs (dict): A dictionary where keys are decades (e.g., '1980s') and values
                                are lists of song dictionaries.

    """
    for decade, songs in organized_songs.items():
        playlist_name = f"{decade} Playlist"
        song_ids = [song["id"] for song in songs]
        create_playlist(spotify_client, playlist_name, song_ids)


def create_monthly_playlists(spotify_client, liked_songs):
    """
    Creates playlists based on the month songs were added to the user's liked songs during the current year.

    Args:
        spotify_client (Spotify): An authenticated Spotipy client.
        liked_songs (dict): A dictionary where keys are song IDs and values are dictionaries
                            containing song information, including 'added_at'.
    """
    current_year = datetime.datetime.now().year
    organized_songs = {}

    # Organize songs by the month they were added to liked songs
    for song_id, song_info in liked_songs.items():
        added_year = int(song_info["added_at"].split("-")[0])

        if added_year == current_year:
            added_month = song_info["added_at"].split("-")[1]

            if added_month not in organized_songs:
                organized_songs[added_month] = []

            organized_songs[added_month].append(song_info)

    # Month names for playlist titles
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

    # Create a playlist for each month
    for month, songs in organized_songs.items():
        playlist_name = f"{month_names[int(month) - 1]} {current_year}"
        song_ids = [song["id"] for song in songs]
        create_playlist(spotify_client, playlist_name, song_ids)
