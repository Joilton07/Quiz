from settings import get_message
from database import players, questions 

def create_player():
    message = get_message("create_user")
    name = input(f"{message}")
    new_player = {"name": name, "score": 0}
    players.append(new_player)

def list_players():
    for player in players:
        print(player["name"])

def create_question():
    message = get_message("create_question")
    question = input(f"{message}")
    new_question = {"question": question}
    questions.append(new_question)

def list_questions():
    for question in questions:
        print(question["question"])
