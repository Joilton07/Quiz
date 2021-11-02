from settings import get_message, SCORE_BY_QUESTION
from database import players, questions 
from utils import divider
from random import choice

def list_questions():
    divider()
    for question in questions:
        print(question["question"])
        for option in question["options"]:
            template_option = "{}. {}" # cria um template
            # insere no template os valores da opção para exibição
            message = template_option.format(option["number"], option["option"])
            
            # caso seja a opção correta insere a sinalização [X]
            if option["correct"]:
                message += "[X]"

            print(message)
    divider()

def play():
    divider()
    message = get_message("select_player")
    player_name = input(f"{message}")
    # p = {"name": [], "score": []}

    player = {}
    print(players)
    for p in players: # busca qual jogador foi selecionado
        if p["name"] == player_name:
            player = p # atualizar a variavel player quando achar o jogar com nome digitado na variavel player_name
    
    question = choice(questions)
    print(question["question"])
    for option in question["options"]:
        template_option = "{}. {}"
        message = template_option.format(option["number"], option["option"])
        print(message)
    
    option_selected_message = get_message("correct_option")
    option_player = int(input(f"{option_selected_message}"))

    option_selected = {}
    # busca a opção do jogador
    for option in question["options"]:
        if option["number"] == option_player:
            option_selected = option
            break
    
    # testa se a opção do jogador está correta
    if option_selected["correct"]:
        player["score"] += SCORE_BY_QUESTION
    else: # caso não esteja exibimos a correta
        for option in question["options"]:
            if option["correct"]:
                message_correct_option = get_message("correct_option")
                option_correct = option["option"]
                print(f"{message_correct_option}: {option_correct}")
    
    divider()