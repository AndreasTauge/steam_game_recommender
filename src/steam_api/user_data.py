import requests 
import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("STEAM_API_KEY")
if not API_KEY:
    raise RuntimeError("STEAM_API_KEY environment variable not set.")

def get_user_games(steamid: str):
    
    URL = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={steamid}&format=json&include_appinfo=1&include_played_free_games=1"
    r = requests.get(URL)
    response = r.json()["response"]
    games_array = response["games"]
    for entry in games_array:
        if entry["playtime_forever"] == 0:
            continue

        print(entry["name"], ": ", entry["playtime_forever"]/60)

get_user_games("76561198131470531")
