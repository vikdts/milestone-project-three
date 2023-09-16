import random


def create_board(grid=5, num_mines=5):
    """
    Takes the arguments to create the functional board with different
    grid size, dependant on the difficulty level of the game.
    """
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
    """
    Welcomes the user to anticipate in the game
    and check out the rules, then prompts the user
    to choose a difficulty level and returns a dictionary
    with the values for the size of the board grid and the
    number of mines or option to exit the game.
    """
    print("""\nHello! This is minesweeper.
Make sure to check out the rules below.
The board is divided into cells, with randomly distributed mines.
Choose the difficulty level, which is based on the grid size.
The number of mines is equal to the size of the grid.
Each level is given three lifes,so if stepping on a mine, can to continue.
The end goal is to clear the board without detonating any mines.
    """)
    user_input = validate_input(
        message="""For Beginner press 'b' grid is 5x5 with 5 mines.
For Intermediate press 'i' grid is 7x7 with 7 mines.
For Expert press 'e' grid is 10x10 with 10 mines.
To exit the game type 'quit'.\n\nUser input:""",
        valid_inputs=('b', 'i', 'e', 'quit')
    )
    if user_input == 'b':
        print('You chose beginner level.\n')
        return {'grid': 5, 'num_mines': 5}

    elif user_input == 'i':
        print('You chose intermediate level.\n')
        return {'grid': 7, 'num_mines': 7}

    elif user_input == 'e':
        print('You chose expert level.\n')
        return {'grid': 10, 'num_mines': 10}
    else:
        print('You exit the game. Thanks for playing.\n')


def validate_input(message, valid_inputs):
    """
    Recursor that validates input.
    """
    user_input = input(message).lower()
    if user_input in valid_inputs:
        return user_input
    else:
        return validate_input(message, valid_inputs)


def play(board, mines_coords, grid, lifes, num_mines):
    """
    Runs the main game loop, where the user tries to guess
    a mine free cell.
    """
    dug = []
    dug_mine = []
    num_cells_win = (grid**2) - num_mines
    exit = False
    while lifes > 0 and len(dug) < num_cells_win:
        try:
            render_board(board)
            user_input = input(f"""\nWhere would you like to dig?
Input from 0 to {grid-1} as row,col.
Type quit if you want to exit the game.\n
User input:""")
            if user_input.lower() == 'quit':
                exit = True
                print("You exit the game.")
                break
            row, col = user_input.split(',')
            row_int = int(row)
            col_int = int(col)
            if any(v not in range(0, grid) for v in (row_int, col_int)):
                raise ValueError
        except ValueError:
            print("Invalid input.\n")
            continue
        if [row_int, col_int] in dug or [row_int, col_int] in dug_mine:
            print("Use new coordinates.")
            continue
        elif [row_int, col_int] in mines_coords:
            lifes -= 1
            print("Stepped on a mine.\n")
            print(f"You have {lifes} lifes left.")
            dig(board, row_int, col_int, dug_mine, '*')
            if lifes > 0:
                choice = validate_input("""Do you want to continue?\n
Press 'y' to continue or
'n' to quit.
User input:""",
                                        ('y', 'n'))
                if choice == 'n':
                    exit = True
                    break
        elif [row_int, col_int] not in mines_coords:
            dig(board, row_int, col_int, dug, '-')

    if exit is True:
        return

    render_board(board)
    win_lose(lifes_left=lifes > 0)


def dig(board, row_coord, col_coord, digging_list, mark):
    """
    Helper function
    """
    board[row_coord][col_coord] = mark
    digging_list.append([row_coord, col_coord])


def win_lose(lifes_left):
    """
    Defines the two outcomes of the game.
    """
    if lifes_left:
        print("Congratulations. It's a win!")
    else:
        print("No more lifes left. Game over.")


def render_board(board):
    """
    Renders the board, to display better experience for the user
    """
    join_rows = []
    nums_top = ' '.join([str(n) for n in range(0, len(board[0]))])

    for index, row in enumerate(board):
        row_to_render = []
        for i in row:
            str_i = str(i)
            row_to_render.append(str_i)
        rendered_row = '|'.join(row_to_render)
        formatted_rendered__row = f"{index} |{rendered_row}|"

        join_rows.append(formatted_rendered__row)
    border_str = ''.join(["-" for _ in join_rows[0]])
    empty_line = ''.join([" " for _ in join_rows[0]])
    join_rows.append(border_str)
    formatted_nums_top = f"   {nums_top}"
    join_rows.insert(0, empty_line)
    join_rows.insert(1, formatted_nums_top)
    join_rows.insert(2, border_str)
    print('\n'.join(join_rows))


def main():
    """
    This function runs the main game loop for Minesweeper.
    First renders the welcome meassage with the rules of the game,
    prompts the player to enter an input of level difficulty, after
    displaying the availble options and the corresponding input to
    initialize the game or exit, if user not engaged.
    The game consists of the player trying to guess the
    coordinates of a cell, without hitting randomly allocated mine.
    If the player guesses a mine-free cell correctly, it is revealed
    on the rendered board with a dash. If guess coordinates step on a
    mine player loses a life, and have to choose if to continue.
    The player wins the game if guesses all the mine free cells,
    before losing all its lifes.
    """
    lifes = 3
    grid_num_mines = say_hello()
    # Returns none to exit the game
    if grid_num_mines is None:
        return
    # takes arguments to create the board size chosen by the user
    board, mines_coord = create_board(grid_num_mines['grid'],
                                      grid_num_mines['num_mines'])
    play(board, mines_coord, grid_num_mines['grid'], lifes,
         grid_num_mines['num_mines'])
    # Ask if player wants to play again
    user_input = validate_input(
        message="""\nDo you want to play again?
Press 'y' to continue or
'n' to exit the game.
User input:""",
        valid_inputs=('y', 'n')
    )
    if user_input == 'y':
        main()


if __name__ == '__main__':
    main()
