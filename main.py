import commands as cmd
from settings import get_message, OPTIONS_BY_QUESTION
from utils import divider

from service import list_questions, play
from services.player_services import create_player, list_players
from services.question_services import create_question, set_correct_option, create_option

def start(command):
    if command == cmd.COMMAND_EXIT:
        return "exit"

    if command == cmd.COMMAND_CREATE_PLAYER:
        divider()
        message = get_message("create_user")
        name = input(f"{message}: ")
        response = create_player(name)
        print(response)
        divider()

    if command == cmd.COMMAND_LIST_PLAYERS:
        divider()
        players = list_players()
        for player in players:
            template = "{} - {}"
            print(template.format(player["name"], str(player["score"])))
        divider()

    if command == cmd.COMMAND_CREATE_QUESTION:
        divider()
        message = get_message("create_question")
        question = input(f"{message}: ")
        new_question = create_question(question)
        for i in range(0, OPTIONS_BY_QUESTION):
            number = i + 1
            message_option = get_message("create_option")
            option = input(f"{message_option} {number}: ")
            new_option = create_option(number, option) # chama a função de criar uma opção para a questão
            new_question["options"].append(new_option)

        message_correct_option = get_message("correct_option")
        option_correct = int(input(f"{message_correct_option}: ")) # solicita a resposta correta
        set_correct_option(option_correct, new_question)
        divider()

    if command == cmd.COMMAND_LIST_QUESTIONS:
        list_questions()
    
    if command == cmd.COMMAND_PLAY:
        play()