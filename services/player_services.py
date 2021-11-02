from database import players

# adiciona um novo jogador do tipo dict na lista players
def create_player(name):
    new_player = {"name": name, "score": 0}
    players.append(new_player)

# list os jogadores da lista players
def list_players():
    return players