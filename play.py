import commands as cmd
from settings  import GAME_NAME
from services import create_player, list_players, create_question, list_questions

run = True

while run:
    commund = input(f"{GAME_NAME} >> ")

    if commund == cmd.COMMAND_EXIT:
         run = False
    if commund == cmd.COMMAND_CREATE_PLAYER:
        create_player()
    if commund == cmd.COMMAND_LIST_PLAYERS:
        list_players()
    if command == cmd.COMMAND_CREATE_QUESTIONS:
        create_question()
    if command == cmd.COMMAND_LIST_QUESTIONS:
        list_questions()