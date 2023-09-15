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
    print("""\nHello! This is minesweeper.
Make sure to check out the rules below.
The board is divided into cells, with randomly distributed mines.
Choose the difficulty level, which is based on the grid size.
The number of mines is equal to the size of the grid.
Each level is given three lives,so if stepping on a mine, can to continue.
The end goal is to clear the board without detonating any mines.
    """)
    user_input = validate_input(
        message="""For Beginner press 'b' grid is 5x5 with 5 mines.
For Intermediate press 'i' grid is 7x7 with 7 mines.
For Expert press 'e' grid is 10x10 with 10 mines.
To exit the game type 'quit'.\n\nUser input:""",
        valid_inputs=('b', 'i', 'e', 'quit')
    )
    # print('user input', user_input)
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
    user_input = input(message).lower()
    if user_input in valid_inputs:
        return user_input
    else:
        return validate_input(message, valid_inputs)


def play(board, mines_coords, grid, lives, num_mines):
    dug = []
    dug_mine = []
    num_cells_win = (grid**2) - num_mines
    exit = False
    while lives > 0 and len(dug) < num_cells_win:
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
            lives -= 1
            print("Stepped on a mine.\n")
            print(f"You have {lives} lives left.")
            dig(board, row_int, col_int, dug_mine, '*')
            if lives > 0:
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
    win_lose(lives_left=lives > 0)


def dig(board, row_coord, col_coord, digging_list, mark):
    board[row_coord][col_coord] = mark
    digging_list.append([row_coord, col_coord])


def win_lose(lives_left):
    if lives_left:
        print("Congratulations. It's a win!")
    else:
        print("No more lives left. Game over.")


def render_board(board):
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
    lives = 3
    grid_num_mines = say_hello()
    if grid_num_mines is None:
        return
    board, mines_coord = create_board(grid_num_mines['grid'],
                                      grid_num_mines['num_mines'])
    play(board, mines_coord, grid_num_mines['grid'], lives,
         grid_num_mines['num_mines'])
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
