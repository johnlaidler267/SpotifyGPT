import os
from ai_analysis.gemini_query import query_gemini, summarize_music_taste
from utils.json_helpers import load_song_data


def main():
    """
    Main function that summarizes the music taste of a person based on their favorite songs.
    """
    # Access the key (from .env file)
    api_key = os.getenv("API_KEY")

    # Load the song data from the JSON file
    json_file = "liked_songs.json"
    song_data = load_song_data(json_file)

    # Stringify the song data
    stringified_music_data = ""

    # Concatenate the title and artist of each song
    for song in song_data.values():
        stringified_music_data += f"{song['title']} by {song['artist']}. "

    summarize_music_taste(song_data)


# Call the main function
main()


if __name__ == "__main__":
    main()
