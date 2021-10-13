GAME_NAME = "QuizGame"
LANG = "pt"

OPTIONS_BY_QUESTION = 4
SCORE_BY_QUESTION = 100

# languages
TEXTS = {
    "eng": {
        "create_user": "User name",
        "create_question": "Question",
        "create_option": "Options",
        "correct_option": "Correct_option",
        "select_player": "Select Player"
    },
    "pt": {
        "create_user": "Nome de usuário",
        "create_question": "Pergunta",
        "create_option": "Opção",
        "correct_option": "Opção correta",
        "select_player": "Selecione o jogador"
    }
}

# pega a mensaga de acorda com a chave do dicionário passada no parâmetro
# leva em consideração da linguagem configuração na variável LANG
def get_message(key):
    return TEXTS[LANG][key]