
from database import questions

def create_option(number, option):
    new_option = {"number": number, "option": option, "correct": False}
    return new_option


# adiciona uma nova questão do tipo dict na lista questions
def create_question(question):
    new_question = {"question": question, "options": []} # cria o dict da question
    questions.append(new_question) # adiciona o dict na lista
    return new_question


def set_correct_option(option_correct, new_question):
    # busca a opção opção selecionada a cima e atribui como correta
    for option in new_question["options"]:
        if option["number"] == option_correct:
            option["correct"] = True
            break # para parar a execução do for