from settings import LANGS, LANG
from database import players

def create_player():
    message = LANGS[LANG]["create_user"]
    name = input(f"{message}")
    new_player = {"name": name, "score": 0}
    players.append(new_player)

def list_players():
    for player in players:
        print(player["name"])