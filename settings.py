GAME_NAME = "QuizGame"
LANG = "eng"

# languages
TEXTS = {
    "eng": {
        "create_user": "User name",
        "create_question": "Question"
    },
    "pt": {
        "create_user": "Nome de usuário",
        "create_question": "Pergunta"
    }
}

def get_message(key):
    return TEXTS[LANG][key]