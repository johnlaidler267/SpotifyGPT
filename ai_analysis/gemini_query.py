import google.generativeai as genai
import sys

sys.path.append("../")
from config.settings import GENAI_API_KEY


def query_gemini(prompt):
    genai.configure(api_key=GENAI_API_KEY)
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text


def summarize_music_taste(song_data):
    stringified_music_data = " ".join(
        [f"{song['title']} by {song['artist']}" for song in song_data.values()]
    )
    prompt = f"Summarize the music taste of the person whose favorite songs are the following: {stringified_music_data}."
    return query_gemini(prompt)
