from settings import GAME_NAME
from main import start

run = True

while run:
    command = input(f"{GAME_NAME} >> ")
    result = start(command)
    if result == "exit":
        run = False