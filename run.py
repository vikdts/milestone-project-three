import random

def create_board(grid=5, num_mines=5):
    cell = 0
    board = [[cell for c in range(grid)]for r in range(grid)]
    mines_coord = []
    plant_mines = 0
    while plant_mines < num_mines:
        loc = random.randint(0, grid**2 - 1)
        row = loc // grid
        col = loc % grid
        if [row, col] in mines_coord:
            continue
        mines_coord.append([row, col])
        plant_mines += 1
    return board, mines_coord


def say_hello():
    while True:
        try:
            user_input = input("Hello! This is minesweeper. \nFor Beginner press 'b', for Intermediate press 'i', for Expert press 'e'. \nTo quit press 'q'.")
        except ValueError:
            print("""Please enter a valid option.
            For Beginner press 'b', for Intermediate press 'i', for Expert press 'e'.
            To quit press 'q'.\n
            """)
            continue
        if user_input == 'b':
            grid = 5
            print(f'You entered: {user_input}. You chose beginner.\n')
        elif user_input == 'i':
            grid = 7
            print(f'You entered: {user_input}. You chose intermediate.\n')
        elif user_input == 'e':
            grid = 10
            print(f'You entered: {user_input}. You chose expert.\n')
        else:
            print(f'You entered: {user_input}. Thanks for playing.\n')