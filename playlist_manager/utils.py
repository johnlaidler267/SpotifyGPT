import json


def save_songs_to_file(song_data, filename="liked_songs.json"):
    with open(filename, "w") as f:
        json.dump(song_data, f, indent=4)


def organize_songs_by_decade(liked_songs):
    organized_songs = {}
    for song_id, song_info in liked_songs.items():
        release_decade = song_info["release_decade"]
        if release_decade not in organized_songs:
            organized_songs[release_decade] = []
        organized_songs[release_decade].append(song_info)
    return organized_songs
