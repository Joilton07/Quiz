from database import questions
from services.questions import create_question

def test_create_question_success():
    questions_len_previous = len(questions)
    create_question("enunciado da questão")
    assert questions_len_previous < len(questions)