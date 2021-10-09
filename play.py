from commands import COMMAND_EXIT
from setting  import GAME_NAME

run = True

while run:
    commund = input(f"{GAME_NAME} >> ")

    if commund == COMMAND_EXIT:
         run = False