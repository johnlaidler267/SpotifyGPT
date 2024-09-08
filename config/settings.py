import os
from dotenv import load_dotenv

# Parse a .env file and then load all the variables found as environment variables.
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = "user-library-read user-library-modify playlist-modify-public"
GENAI_API_KEY = os.getenv("API_KEY")
