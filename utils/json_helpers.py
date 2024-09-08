import json


def load_song_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)


def save_songs_to_file(song_data, filename="liked_songs.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(song_data, f, indent=4)
