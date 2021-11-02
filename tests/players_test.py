from services.players import create_player, list_players
from database import players

def test_create_player_success():
    previous_players_length = len(players)
    create_player("Leonardo")
    assert previous_players_length < len(players)
    assert create_player("Leonardo") == "Jogador cadastrado com sucesso"

def test_create_player_error():
    previous_players_length = len(players)
    create_player(10)
    assert previous_players_length == len(players)
    create_player("jo")
    assert previous_players_length == len(players)
    assert create_player("jo") == "Nome inválido"


def test_list_players_success():
    players = list_players()
    assert type(players) == list
    create_player("Leonardo")