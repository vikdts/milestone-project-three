# Minesweeper

Minesweeper is a classic and popular online puzzle single player game. It is all age appropriate. This is not the classic version, which offers clues with numbers of neighboring mines. The outcome depends on random events, to clear the board without detonating any mines.
The game begins with introduction to the game rules and selection of a difficulty level, beginner internediate or expert, which is based on the grid size. 

Once selected the difficulty level, it renders a board with the hidden cells all marked with '0'. The user is prompted to choose a cell to dig, by giving an input, according to the
row and column number. If correct and no mine was detonated, a message will indicate to 
continue with new location to dig and the board, will be rendered with the cleared cell,
marked with '-'. However, if the user guesses incorrectly, there will be rendered a message
for hitting a mine. All difficulty levels are given three lives, so the user will be propted
to choose to continue the game or quit. In ordered to win the player has to clear the board,
before running out of lives.

Minesweeper is an interesting and familiar game, that keeps the player engaged, based on simple guessing skills. It is a great way to have some fun and mine-out!

## How to play

In this implementation of Minesweeper you will be prompted to
choose a difficulty level, based on the grid size. The computer will
render a board either 5x5, 7x7 or 10x10 accordingly the level diffuculty,
and randomly distribute mines, corresponding their number to the grid size.
You will have to guess all the coordinates, avoiding to step on the mines,
to clear the board without detonating any mines and win the game.

## Logic Flowchart
![Flowchart](./images/flowchart.jpg)