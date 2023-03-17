import tkinter as tk
import numpy as np

# Define the game board dimensions
ROWS = 6
COLUMNS = 7

# Define the players
PLAYER1 = 1
PLAYER2 = 2

# Define the colors for the players
COLORS = {
    PLAYER1: "red",
    PLAYER2: "yellow"
}

# Initialize the game board with zeros
board = np.zeros((ROWS, COLUMNS), dtype=int)

# Initialize the player
current_player = PLAYER1

# Define a function to drop a disc in a column
def drop_disc(column):
    global current_player

    # Check if the column is valid
    if not is_valid_move(column):
        return

    # Get the row for the new disc
    row = get_next_row(column)

    # Update the board and draw the new disc
    board[row][column] = current_player
    canvas.create_oval(column * 80 + 10, row * 80 + 10, column * 80 + 70, row * 80 + 70, fill=COLORS[current_player])

    # Check if the game is over
    if check_win():
        message = f"Player {current_player} wins!"
        canvas.create_text(COLUMNS * 40, ROWS * 40 + 20, text=message, font=("Arial", 24))
        return

    if np.all(board != 0):
        message = "It's a tie!"
        canvas.create_text(COLUMNS * 40, ROWS * 40 + 20, text=message, font=("Arial", 24))
        return

    # Switch to the next player
    current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1

# Define a function to check if a move is valid
def is_valid_move(column):
    return board[ROWS-1][column] == 0

# Define a function to get the next available row in a column
def get_next_row(column):
    for row in range(ROWS):
        if board[row][column] == 0:
            return row

# Define a function to check if a player has won
def check_win():
    # Check horizontally
    for row in range(ROWS):
        for column in range(COLUMNS-3):
            if board[row][column] == current_player and board[row][column+1] == current_player and board[row][column+2] == current_player and board[row][column+3] == current_player:
                return True

    # Check vertically
    for row in range(ROWS-3):
        for column in range(COLUMNS):
            if board[row][column] == current_player and board[row+1][column] == current_player and board[row+2][column] == current_player and board[row+3][column] == current_player:
                return True

    # Check diagonally (up-right)
    for row in range(ROWS-3):
        for column in range(COLUMNS-3):
            if board[row][column] == current_player and board[row+1][column+1] == current_player and board[row+2][column+2] == current_player and board[row+3][column+3] == current_player:
                return True

    # Check diagonally (up-left)
    for row in range(ROWS-3):
        for column in range(3, COLUMNS):
            if board[row][column] == current_player and board[row+1][column-1] == current_player and board[row+2][column-2] == current_player and board[row+3][column-3] == current_player:
                return True

    # No win found
    return False

# Define a function to reset the game
def reset():
    global board, current_player
    board = np.zeros((ROWS, COLUMNS), dtype=int)
    current_player = PLAYER1
    canvas.delete("all")
    draw_board()

# Define a function to draw the game board
def draw_board():
    for row in range(ROWS):
        for column in range(COLUMNS):
            canvas.create_rectangle(column * 80, row * 80, column * 80 + 80, row * 80 + 80, fill="blue")

# Create the main window
root = tk.Tk()
root.title("Connect Four")

# Create the canvas to draw the game board and discs
canvas = tk.Canvas(root, width=COLUMNS * 80, height=ROWS * 80 + 50)
canvas.pack()

# Draw the game board
draw_board()

# Create the "Reset" button
button = tk.Button(root, text="Reset", command=reset)
button.pack()

# Bind the column buttons to the drop_disc function
for column in range(COLUMNS):
    button = tk.Button(root, text="Drop", command=lambda column=column: drop_disc(column))
    button.pack()

# Start the main loop
root.mainloop()