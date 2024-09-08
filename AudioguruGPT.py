import json
import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Function to load the JSON file containing the song data
def load_song_data(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        song_data = json.load(f)
    return song_data


# Function to query Gemini Pro's model for summaries and answers
def query_gemini(prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt])
    print(response.text)


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

    print(stringified_music_data)

    # Generate a prompt for the song
    prompt = f"Summarize the music taste of the person who's favorite songs are the following '{stringified_music_data}."
    summary = query_gemini(prompt, api_key)
    print(f"Summary: {summary}")


# Call the main function
main()


if __name__ == "__main__":
    main()
