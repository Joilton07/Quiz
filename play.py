from commands import COMMAND_EXIT, COMMAND_CREATE_PLAYER
from setting  import GAME_NAME, LANG, LANGS

run = True
player = []

while run:
    commund = input(f"{GAME_NAME} >> ")

    if commund == COMMAND_EXIT:
         run = False
    if commund == COMMAND_CREATE_PLAYER:
        message = LANGS[LANG]["create_user"]
        name = input(f"{message}: ")