import commands as cmd
from settings  import GAME_NAME
from services import create_player, list_players, create_question, list_questions, play

run = True

while run:
    command = input(f"{GAME_NAME} >> ")

    if command == cmd.COMMAND_EXIT:
         run = False
    if command == cmd.COMMAND_CREATE_PLAYER:
        create_player()
    if command == cmd.COMMAND_LIST_PLAYERS:
        list_players()
    if command == cmd.COMMAND_CREATE_QUESTION:
        create_question()
    if command == cmd.COMMAND_LIST_QUESTIONS:
        list_questions()
    if command == cmd.COMMAND_PLAY:
        play()
