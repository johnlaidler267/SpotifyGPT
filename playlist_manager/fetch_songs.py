def fetch_liked_songs(spotify_client):
    """
    Fetch the user's liked songs from Spotify using the provided Spotify client.

    Args:
        spotify_client (Spotify): An authenticated Spotipy client.

    Returns:
        dict: A dictionary containing liked songs, where each key is the song ID and the value is a dictionary
        containing song information.
    """
    liked_songs = {}
    results = spotify_client.current_user_saved_tracks(limit=50)

    # Loop through all pages of results
    while results:
        # Extract song info from each track in the current page of results
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

        # Paginate through additional tracks if available
        if results["next"]:
            results = spotify_client.next(results)
        else:
            break

    return liked_songs
