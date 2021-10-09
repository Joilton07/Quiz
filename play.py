from commands import (
    COMMAND_EXIT, 
    COMMAND_CREATE_PLAYER,
    COMMAND_LIST_PLAYERS
)
from settings  import GAME_NAME
from services import create_player, list_players

run = True

while run:
    commund = input(f"{GAME_NAME} >> ")

    if commund == COMMAND_EXIT:
         run = False
    if commund == COMMAND_CREATE_PLAYER:
        create_player()
    if commund == COMMAND_LIST_PLAYERS:
        list_players()