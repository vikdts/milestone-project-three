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


def validate_input():
    pass


def play(board, mines_coords, grid, lives, num_mines):
    dug = []
    dug_mine = []
    num_cells_win = (grid**2) - num_mines
    exit = False
    while lives > 0 and len(dug)< num_cells_win:
        try:
            # print(len(dug), num_mines, lives, num_cells_win)
            # print(mines_coords)
            render_board(board)
            user_input = input(f"Choose a place to dig 0-{grid-1} , ex. row,col - 2,3.\nType quit if you wanna exit the game.\n")
            if user_input == 'quit':
                exit = True
                print("You exit the game.")
                break
            row, col = user_input.split(',')
            row_int = int(row)
            col_int = int(col)
            if col_int >= grid or row_int >= grid:
                raise ValueError
        except ValueError:
            print("Invalid input")
            continue
        if [row_int, col_int] in dug or [row_int, col_int] in dug_mine:
            print("Use new coordinates")
            continue
        elif [row_int, col_int] in mines_coords:
            lives -= 1
            print("Stepped on a mine.")
            print(f"Lives left {lives}")
            board[row_int][col_int] = '*'
            dug_mine.append([row_int, col_int])
            choice = validate_input('Do you want to continue? Press "y" to continue and "no: to exit the game.\n', ('y', 'n'))
            if choice == 'n':
                exit = True
                break
        elif [row_int, col_int] not in mines_coords:
            board[row_int][col_int] = '-'
            dug.append([row_int, col_int])
    if exit is True:
        return
    render_board(board)
    win_lose(num_cells_dug=len(dug), num_cells_win=num_cells_win)



def win_lose():
    pass


def render_board():
    pass

